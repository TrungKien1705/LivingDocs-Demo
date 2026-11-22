"""Module xử lý logic tính giá và khuyến mãi cho đơn hàng."""

DEFAULT_TAX_RATE = 0.08  # Thuế VAT mặc định 10%


def calculate_discount(subtotal: float, coupon_code: str | None = None) -> float:
    """Tính số tiền được giảm giá dựa trên mã khuyến mãi.

    Args:
        subtotal (float): Tổng tiền hàng trước khi giảm giá (VNĐ).
        coupon_code (str | None): Mã giảm giá (VD: 'SAVE10', 'SAVE20').

    Returns:
        float: Số tiền được giảm (VNĐ).
    """
    if not coupon_code:
        return 0.0

    discounts = {
        "SAVE10": 0.10,
        "SAVE20": 0.20,
    }
    rate = discounts.get(coupon_code.upper(), 0.0)
    return subtotal * rate


def calculate_final_price(
    subtotal: float,
    coupon_code: str | None = None,
    tax_rate: float = DEFAULT_TAX_RATE,
) -> dict:
    """Tính tổng tiền cuối cùng của đơn hàng sau giảm giá và thuế.

    Args:
        subtotal (float): Tổng tiền hàng ban đầu.
        coupon_code (str | None): Mã giảm giá áp dụng (nếu có).
        tax_rate (float): Thuế suất VAT (mặc định 0.1 tương ứng 10%).

    Returns:
        dict: Chi tiết gồm subtotal, discount, tax và final_total.
    """
    if subtotal < 0:
        raise ValueError("Tổng tiền hàng không được âm.")

    discount = calculate_discount(subtotal, coupon_code)
    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_rate
    final_total = taxable_amount + tax

    return {
        "subtotal": subtotal,
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "final_total": round(final_total, 2),
    }
