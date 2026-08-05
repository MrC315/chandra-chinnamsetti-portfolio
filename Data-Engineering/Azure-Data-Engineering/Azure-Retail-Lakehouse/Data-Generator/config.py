from pathlib import Path


# ---------------------------------------------------------
# PROJECT SETTINGS
# ---------------------------------------------------------

PROJECT_NAME = "Azure Retail Lakehouse"
COMPANY_NAME = "Contoso Retail"


# ---------------------------------------------------------
# OUTPUT SETTINGS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

CSV_ENCODING = "utf-8"
RANDOM_SEED = 42


# ---------------------------------------------------------
# DATA VOLUME SETTINGS
# ---------------------------------------------------------

NUMBER_OF_CUSTOMERS = 10_000
NUMBER_OF_PRODUCTS = 500
NUMBER_OF_STORES = 25
NUMBER_OF_SALES = 100_000
NUMBER_OF_RETURNS = 6_500


# ---------------------------------------------------------
# DATE SETTINGS
# ---------------------------------------------------------

SALES_START_DATE = "2023-01-01"
SALES_END_DATE = "2026-07-31"


# ---------------------------------------------------------
# BUSINESS SETTINGS
# ---------------------------------------------------------

CUSTOMER_SEGMENTS = [
    "Consumer",
    "Corporate",
    "Small Business",
]

SALES_CHANNELS = [
    "Store",
    "Online",
    "Mobile App",
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "PayPal",
    "Gift Card",
    "Cash",
]

ORDER_STATUSES = [
    "Completed",
    "Cancelled",
    "Pending",
]

RETURN_REASONS = [
    "Damaged",
    "Wrong Item",
    "Not Needed",
    "Quality Issue",
    "Late Delivery",
    "Size/Fit",
]

PRODUCT_CATEGORIES = [
    "Electronics",
    "Home & Kitchen",
    "Clothing",
    "Footwear",
    "Beauty",
    "Sports & Outdoors",
    "Toys & Games",
    "Grocery",
    "Office Supplies",
    "Automotive",
    "Books",
    "Pet Supplies",
]

US_REGIONS = {
    "Midwest": ["MI", "IL", "OH", "IN"],
    "Northeast": ["NY", "MA", "PA"],
    "South": ["GA", "TX", "NC", "TN", "FL"],
    "West": ["CO", "AZ", "WA", "OR", "CA", "NV", "UT"],
}


# ---------------------------------------------------------
# DATA QUALITY SETTINGS
# ---------------------------------------------------------

MISSING_EMAIL_PERCENTAGE = 0.01
MISSING_PHONE_PERCENTAGE = 0.02
DISCONTINUED_PRODUCT_PERCENTAGE = 0.10
CANCELLED_ORDER_PERCENTAGE = 0.02
PENDING_ORDER_PERCENTAGE = 0.02
