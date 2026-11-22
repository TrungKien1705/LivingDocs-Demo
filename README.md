# LivingDocs-Demo (Order Pricing API)

Dịch vụ tính giá đơn hàng đơn giản bằng Python (FastAPI) dùng để demo hệ thống **LivingDocs**.

## Quy tắc nghiệp vụ hiện tại
- **Thuế VAT mặc định:** 10% (`DEFAULT_TAX_RATE = 0.1`).
- **Mã giảm giá hỗ trợ:**
  - `SAVE10`: Giảm 10% tổng tiền hàng.
  - `SAVE20`: Giảm 20% tổng tiền hàng.

## Danh sách API
- `GET /health`: Kiểm tra trạng thái server.
- `POST /orders/calculate`: Tính tổng tiền đơn hàng từ `subtotal` và `coupon_code`.