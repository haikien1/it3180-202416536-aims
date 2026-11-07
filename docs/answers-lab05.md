
# Trả lời thảo luận Lab 05

## 1. Upstream first vs Release first?

- **Upstream first (Sửa master trước, cherry-pick về release):**
  - **Ưu điểm:** Không bao giờ quên cập nhật bản sửa lỗi cho các tính năng tương lai.
  - **Nhược điểm:** Dễ bị xung đột (conflict) hoặc không tương thích khi mang ngược một đoạn code từ môi trường mới nhất về môi trường cũ.

- **Release first (Sửa release trước, cherry-pick về master – Cách Lab 05 làm):**
  - **Ưu điểm:** Cứu khách hàng ngay lập tức trên môi trường bản cũ, đảm bảo độ tương thích với phiên bản đang phát hành.
  - **Nhược điểm:** Lập trình viên dễ quên thao tác cherry-pick để mang bản vá lên nhánh `master` hoặc các nhánh release tương lai, khiến lỗi tái xuất hiện ở bản cập nhật sau.

## 2. Nếu quên lan truyền lỗi sang release/lab05, lệnh kiểm toán nào phát hiện?

- **Kiểm tra bằng Git:** Lệnh `git tag --contains <FIX_SHA>` sẽ liệt kê các tag chứa commit sửa lỗi. Nếu chỉ xuất hiện `v1.0.1` mà không có `v1.1.0`, có thể bản vá chưa được lan truyền sang phiên bản mới.
- **Kiểm tra bằng script:** Chạy script kiểm thử sẽ thấy nhánh `v1.1.0` trả về 0 kết quả (Fail) thay vì 1 (Pass), qua đó phát hiện lỗi chưa được sửa trên phiên bản mới.
