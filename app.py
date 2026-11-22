"""API đơn giản cho dịch vụ tính giá đơn hàng."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pricing import calculate_final_price

app = FastAPI(title="Order Pricing API", version="1.0.0")


class OrderRequest(BaseModel):
    subtotal: float
    coupon_code: str | None = None


@app.get("/health")
def health_check() -> dict:
    """Kiểm tra trạng thái hoạt động của dịch vụ."""
    return {"status": "ok", "service": "order-pricing-api"}


@app.post("/orders/calculate")
def calculate_order(order: OrderRequest) -> dict:
    """Tính tổng tiền cuối cùng cho một đơn hàng.

    Args:
        order (OrderRequest): Dữ liệu đơn hàng gồm subtotal và coupon_code.

    Returns:
        dict: Bảng kê chi tiết giá, giảm giá, thuế và tổng cộng.
    """
    try:
        return calculate_final_price(
            subtotal=order.subtotal,
            coupon_code=order.coupon_code,
        )
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))