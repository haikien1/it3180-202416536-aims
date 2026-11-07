# TODO-mini

Ứng dụng dòng lệnh Python quản lý danh sách công việc (chỉ dùng thư viện chuẩn,
kiểm thử bằng `unittest`). Dự án nhỏ, được dùng để thực hành **quản lý cấu hình
phần mềm với Git & GitHub** (môn IT3180).

## Chạy

```bash
python main.py
python -m unittest discover -s tests -v
```

## Quy tắc nhánh (Release Flow rút gọn)

| Nhánh | Đặt tên | Tạo từ | Merge vào | Mục đích |
|-------|---------|--------|-----------|----------|
| feature / topic | `feature/<tên>`, `topic/<mô-tả>` | master | master | Tính năng / chủ đề |
| bugfix | `bugfix/<mô-tả>` | master / feature | master / feature | Sửa lỗi khi phát triển |
| refactor | `refactor/<mô-tả>` | master / feature | master / feature | Tái cấu trúc |
| release | `release/labXX` | master | không | Nộp bài / đóng băng baseline |
| hotfix | `hotfix/<mô-tả>` | release | release & master | Sửa bản đã phát hành |

Không commit trực tiếp lên `master` và `release/*`. Mọi thay đổi đi qua Pull Request.

Commit message theo Conventional Commits: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `ci`.
