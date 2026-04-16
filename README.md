# 🗺️ Hệ thống Tìm đường Sankt-Peterburg - Core Data Module

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OSMnx](https://img.shields.io/badge/Library-OSMnx-green)
![NetworkX](https://img.shields.io/badge/Library-NetworkX-orange)

Đây là kho chứa mã nguồn cốt lõi (Core Module) phục vụ cho Đồ án Trí tuệ Nhân tạo. Module này chịu trách nhiệm thu thập, xử lý và cung cấp toàn bộ dữ liệu mạng lưới đường phố và giao thông công cộng tại Sankt-Peterburg để làm đầu vào cho các thuật toán tìm đường (A*, BFS, v.v.).

## ✨ Tính năng của Module Dữ liệu (`map_data.py`)

* **Tự động tải bản đồ:** Lấy dữ liệu đồ thị đường phố thực tế (chỉ dành cho xe cộ) từ OpenStreetMap trong bán kính 2km.
* **Định tuyến tọa độ:** Tìm kiếm và trả về ID của Node giao cắt gần nhất dựa trên tọa độ vĩ độ/kinh độ (hỗ trợ cho thao tác click chuột trên UI).
* **Quét trạm giao thông:** Trích xuất tự động danh sách các ga tàu hỏa, tàu điện ngầm (Subway) trong khu vực để kết xuất lên giao diện đồ họa.

## 🛠️ Cài đặt Môi trường

Để sử dụng module này, máy tính cần cài đặt các thư viện lõi xử lý dữ liệu không gian. Chạy lệnh sau tại thư mục gốc:

```bash
pip install -r requirements.txt