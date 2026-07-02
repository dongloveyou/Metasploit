# Metasploit Automation Tool (CLI)

Một công cụ giao diện dòng lệnh (CLI) được phát triển bằng ngôn ngữ Python nhằm tự động hóa quy trình cấu hình, khởi tạo tham số và quản lý các tác vụ kiểm thử an toàn thông tin cơ bản trong môi trường Lab. 

Công cụ được thiết kế linh hoạt với giao diện trực quan, đồng bộ mã màu hệ thống và tích hợp **Chế độ mô phỏng (Simulation Mode)** để đảm bảo luồng chạy không bị gián đoạn ngay cả khi môi trường thử nghiệm thiếu các gói dịch vụ phụ thuộc.

---

## 📦 Cài đặt các gói thư viện Python (Quan trọng nhất)

Để công cụ hiển thị chính xác giao diện màu sắc ANSI và thực hiện các yêu cầu truy vấn mạng mà không gặp lỗi hệ thống, bạn cần cài đặt các thư viện sau thông qua trình quản lý gói `pip`:

```bash
pip install colorama requests
## 🚀 Hướng dẫn cài đặt và khởi chạy nhanh (Tất cả nền tảng)

Áp dụng chung cho **Termux (Android)**, **Kali Linux**, và **Windows**. Hãy mở Terminal / Command Prompt của thiết bị lên và chạy lần lượt các lệnh sau:

### Bước 1: Tải mã nguồn về máy
```bash
git clone [https://github.com/dongloveyou/Metasploit.git](https://github.com/dongloveyou/Metasploit.git)
cd Metasploit
Trên Kali Linux / Ubuntu (Cần quyền root):
sudo python main.py


Công cụ này được phát triển hoàn toàn vì mục đích giáo dục, nghiên cứu học tập kỹ thuật lập trình và thử nghiệm an toàn thông tin trong các môi trường Lab hợp pháp. Tác giả hoàn toàn không chịu trách nhiệm đối với bất kỳ hành vi hoặc hậu quả nào do việc sử dụng công cụ sai mục đích gây ra


