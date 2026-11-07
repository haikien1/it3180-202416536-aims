
# Trả lời câu hỏi thảo luận Lab 04

## 1. Vì sao release/* không bao giờ merge ngược vào master?

- **Nguyên tắc:** Nhánh `release/*` là nhánh đóng băng để bảo trì một phiên bản cụ thể. Nếu ta merge toàn bộ nhánh `release/*` vào `master`, ta có thể vô tình làm rối loạn cấu trúc hoặc đè lên các tính năng mới đang được phát triển tích cực trên `master`.
- **Giải pháp:** Nếu có lỗi (bug) trên `release`, ta tạo nhánh `hotfix` và dùng lệnh `cherry-pick` để nhặt đúng commit sửa lỗi đó đưa về `master`.

## 2. So sánh quy trình này với GitFlow?

- **GitFlow:** Dùng nhánh `develop` để tích hợp tính năng hàng ngày và nhánh `master` chỉ để lưu các bản đã phát hành.
- **Release Flow (của học phần):** Chỉ có một nhánh chính sống lâu dài là `master`. Khi cần phát hành, ta tách nhánh `release/*` từ `master` ra để ổn định và bảo trì.
- **Ưu điểm:** Cách này giúp nhánh sống ngắn hơn, giữ mọi thứ gần `master` nhất có thể và tránh được tình trạng "merge hell".

## 3. Vì sao nâng lên 1.0.0 mà không phải 0.4.0?

- **Theo Semantic Versioning (SemVer):** Các phiên bản bắt đầu bằng `0.y.z` là giai đoạn phát triển ban đầu, mã nguồn chưa ổn định và API có thể thay đổi liên tục.
- **Lý do nâng phiên bản:** Khi ứng dụng đạt mốc ổn định, hoàn thiện các tính năng cốt lõi và sẵn sàng xuất bản/nộp bài, ta nâng phiên bản MAJOR lên `1.0.0` để đánh dấu việc kết thúc giai đoạn phát triển ban đầu và cam kết về tính ổn định của API.
