import subprocess
import time

# лого
print('''
///   ///   ////    ///  /    ///    ///    ///////   ///
 /// /// //////    ///  //   ///    ///    ///       ///
  ////     ///    /// // // ///    ///    ///////   /// 
   /      ///     ///    ///      ///    ///       ///
''')

# забей
processes = [] 

# переменные
num = int(input('Введите количество фейковых сетей: '))
name = input('Введите название фейковых сетей: ')
wlanname = input('Введите название wlan: ')

# скрипт для создания mon<N>
result = subprocess.run(
    ['./bash.sh', str(num), name, wlanname],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("Вывод скрипта:")
print(result.stdout)

# переменные
mon = 0
ch = 1
mac = '00:11:22:33:44:01'

# цикл для создание фейк сетей с разными именами, mac адресом и постоянно меняющим каналом всех фейк сетей(Все сети с wpa защитой)

for i in range(num):
    namestr = f"{name}({i})"
    macstr = f'00:11:22:33:44:{i:02x}'
    monstr = f"mon{i}"
    chstr = f"{ch}"
    mon += 1

    cmd = [
        "sudo",
        "airbase-ng",
        "-e", namestr,
        "-c", chstr,
        "-a", macstr,
        monstr,
        '-z', "2"
    ]

    ch += 1

    proc = subprocess.Popen(cmd)
    processes.append(proc)

print('Все сети запущены. Нажмите Ctrl+C, чтобы выключить скрипт и все сети.')

# остановка скрипта и сетей, а также вечное выполнение команды airdump-ng

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('\nОстановка по Ctrl+C...')
    for p in processes:
        p.terminate()
        try:
            p.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()
            p.communicate()
    print('Все процессы завершены.')