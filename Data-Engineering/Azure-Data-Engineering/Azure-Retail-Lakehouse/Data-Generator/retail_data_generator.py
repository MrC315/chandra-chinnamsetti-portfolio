from __future__ import annotations

import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

import config


fake = Faker("en_US")

random.seed(config.RANDOM_SEED)
np.random.seed(config.RANDOM_SEED)
Faker.seed(config.RANDOM_SEED)


def ensure_output_directory() -> None:
    """Create the output directory if it does not exist."""
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def random_date(start_date: str, end_date: str) -> datetime:
    """Generate a random date between two YYYY-MM-DD values."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))


def generate_categories() -> pd.DataFrame:
    records = []

    for index, category_name in enumerate(
        config.PRODUCT_CATEGORIES,
        start=1,
    ):
        records.append(
            {
                "category_id": f"CAT{index:03d}",
                "category_name": category_name,
            }
        )

    return pd.DataFrame(records)


def generate_stores() -> pd.DataFrame:
    records = []

    for store_number in range(1, config.NUMBER_OF_STORES + 1):
        region = random.choice(list(config.US_REGIONS.keys()))
        state = random.choice(config.US_REGIONS[region])

        records.append(
            {
                "store_id": f"ST{store_number:03d}",
                "store_name": f"{fake.city()} Retail Store",
                "city": fake.city(),
                "state": state,
                "region": region,
                "store_size": random.choice(
                    ["Small", "Medium", "Large"]
                ),
                "open_date": fake.date_between(
                    start_date="-15y",
                    end_date="-1y",
                ).isoformat(),
                "manager_name": fake.name(),
                "store_status": random.choices(
                    ["Active", "Temporarily Closed"],
                    weights=[98, 2],
                    k=1,
                )[0],
            }
        )

    return pd.DataFrame(records)


def generate_products(
    categories: pd.DataFrame,
) -> pd.DataFrame:
    product_types = [
        "Smart Speaker",
        "Wireless Headphones",
        "Coffee Maker",
        "Running Shoes",
        "Winter Jacket",
        "Backpack",
        "Desk Chair",
        "Skin Serum",
        "Board Game",
        "Pet Bed",
        "Notebook",
        "Vacuum Cleaner",
    ]

    brands = [
        "NorthStar",
        "UrbanPeak",
        "NovaTech",
        "EverHome",
        "PureLife",
        "TrailWorks",
        "BrightKids",
        "DailyChoice",
    ]

    category_ids = categories["category_id"].tolist()

    records = []

    for product_number in range(
        1,
        config.NUMBER_OF_PRODUCTS + 1,
    ):
        unit_cost = round(random.uniform(3, 450), 2)
        unit_price = round(
            unit_cost * random.uniform(1.20, 2.40),
            2,
        )

        discontinued = (
            random.random()
            < config.DISCONTINUED_PRODUCT_PERCENTAGE
        )

        records.append(
            {
                "product_id": f"PRD{product_number:05d}",
                "product_name": (
                    f"{random.choice(brands)} "
                    f"{random.choice(product_types)} "
                    f"{product_number:03d}"
                ),
                "category_id": random.choice(category_ids),
                "brand": random.choice(brands),
                "unit_cost": unit_cost,
                "unit_price": unit_price,
                "product_status": (
                    "Discontinued"
                    if discontinued
                    else "Active"
                ),
                "launch_date": fake.date_between(
                    start_date="-8y",
                    end_date="today",
                ).isoformat(),
            }
        )

    return pd.DataFrame(records)


def generate_customers() -> pd.DataFrame:
    states = [
        state
        for region_states in config.US_REGIONS.values()
        for state in region_states
    ]

    records = []

    for customer_number in range(
        1,
        config.NUMBER_OF_CUSTOMERS + 1,
    ):
        first_name = fake.first_name()
        last_name = fake.last_name()

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}."
            f"{customer_number}@example.com"
        )

        phone = fake.phone_number()

        if random.random() < config.MISSING_EMAIL_PERCENTAGE:
            email = None

        if random.random() < config.MISSING_PHONE_PERCENTAGE:
            phone = None

        records.append(
            {
                "customer_id": f"CUST{customer_number:06d}",
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "city": fake.city(),
                "state": random.choice(states),
                "postal_code": fake.postcode(),
                "customer_segment": random.choice(
                    config.CUSTOMER_SEGMENTS
                ),
                "loyalty_tier": random.choices(
                    ["Bronze", "Silver", "Gold", "Platinum"],
                    weights=[45, 30, 18, 7],
                    k=1,
                )[0],
                "signup_date": fake.date_between(
                    start_date="-7y",
                    end_date="today",
                ).isoformat(),
                "customer_status": random.choices(
                    ["Active", "Inactive"],
                    weights=[96, 4],
                    k=1,
                )[0],
            }
        )

    return pd.DataFrame(records)


def choose_order_status() -> str:
    value = random.random()

    if value < config.CANCELLED_ORDER_PERCENTAGE:
        return "Cancelled"

    if value < (
        config.CANCELLED_ORDER_PERCENTAGE
        + config.PENDING_ORDER_PERCENTAGE
    ):
        return "Pending"

    return "Completed"


def seasonal_multiplier(sale_date: datetime) -> float:
    month = sale_date.month

    if month in [11, 12]:
        return 1.35

    if month in [6, 7]:
        return 1.10

    if month in [1, 2]:
        return 0.90

    return 1.00


def generate_sales(
    customers: pd.DataFrame,
    products: pd.DataFrame,
    stores: pd.DataFrame,
) -> pd.DataFrame:
    customer_ids = customers["customer_id"].tolist()
    store_ids = stores["store_id"].tolist()

    product_ids = products["product_id"].tolist()
    product_lookup = (
        products
        .set_index("product_id")
        .to_dict("index")
    )

    records = []

    for sale_number in range(
        1,
        config.NUMBER_OF_SALES + 1,
    ):
        sale_date = random_date(
            config.SALES_START_DATE,
            config.SALES_END_DATE,
        )

        product_id = random.choice(product_ids)
        product = product_lookup[product_id]

        quantity = random.choices(
            [1, 2, 3, 4, 5],
            weights=[55, 25, 12, 5, 3],
            k=1,
        )[0]

        discount_pct = random.choices(
            [0, 5, 10, 15, 20, 25, 30],
            weights=[35, 15, 20, 12, 10, 5, 3],
            k=1,
        )[0]

        multiplier = seasonal_multiplier(sale_date)

        unit_price = round(
            float(product["unit_price"]) * multiplier,
            2,
        )

        unit_cost = round(
            float(product["unit_cost"]),
            2,
        )

        gross_amount = round(
            unit_price * quantity,
            2,
        )

        discount_amount = round(
            gross_amount * discount_pct / 100,
            2,
        )

        net_sales = round(
            gross_amount - discount_amount,
            2,
        )

        total_cost = round(
            unit_cost * quantity,
            2,
        )

        profit = round(
            net_sales - total_cost,
            2,
        )

        records.append(
            {
                "sale_id": f"SALE{sale_number:08d}",
                "order_id": (
                    f"ORD{((sale_number - 1) // 2) + 1:08d}"
                ),
                "sale_date": sale_date.date().isoformat(),
                "customer_id": random.choice(customer_ids),
                "product_id": product_id,
                "store_id": random.choice(store_ids),
                "sales_channel": random.choice(
                    config.SALES_CHANNELS
                ),
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_pct": discount_pct,
                "gross_amount": gross_amount,
                "discount_amount": discount_amount,
                "net_sales": net_sales,
                "unit_cost": unit_cost,
                "total_cost": total_cost,
                "profit": profit,
                "payment_method": random.choice(
                    config.PAYMENT_METHODS
                ),
                "order_status": choose_order_status(),
                "source_system": "RetailPOS",
                "ingestion_created_at": (
                    datetime.utcnow().isoformat()
                ),
            }
        )

    return pd.DataFrame(records)


def generate_returns(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    completed_sales = sales[
        sales["order_status"] == "Completed"
    ].copy()

    return_count = min(
        config.NUMBER_OF_RETURNS,
        len(completed_sales),
    )

    selected_sales = completed_sales.sample(
        n=return_count,
        random_state=config.RANDOM_SEED,
    )

    records = []

    for return_number, sale in enumerate(
        selected_sales.itertuples(index=False),
        start=1,
    ):
        original_date = datetime.strptime(
            sale.sale_date,
            "%Y-%m-%d",
        )

        return_date = original_date + timedelta(
            days=random.randint(1, 45)
        )

        return_quantity = random.randint(
            1,
            max(1, int(sale.quantity)),
        )

        refund_amount = round(
            float(sale.net_sales)
            * return_quantity
            / max(1, int(sale.quantity)),
            2,
        )

        records.append(
            {
                "return_id": f"RET{return_number:07d}",
                "sale_id": sale.sale_id,
                "return_date": return_date.date().isoformat(),
                "return_reason": random.choice(
                    config.RETURN_REASONS
                ),
                "return_quantity": return_quantity,
                "refund_amount": refund_amount,
                "refund_status": random.choices(
                    ["Refunded", "Pending", "Rejected"],
                    weights=[92, 6, 2],
                    k=1,
                )[0],
            }
        )

    return pd.DataFrame(records)


def validate_relationships(
    customers: pd.DataFrame,
    products: pd.DataFrame,
    stores: pd.DataFrame,
    sales: pd.DataFrame,
    returns: pd.DataFrame,
) -> None:
    if not sales["customer_id"].isin(
        customers["customer_id"]
    ).all():
        raise ValueError("Invalid customer IDs in sales.")

    if not sales["product_id"].isin(
        products["product_id"]
    ).all():
        raise ValueError("Invalid product IDs in sales.")

    if not sales["store_id"].isin(
        stores["store_id"]
    ).all():
        raise ValueError("Invalid store IDs in sales.")

    if not returns["sale_id"].isin(
        sales["sale_id"]
    ).all():
        raise ValueError("Invalid sale IDs in returns.")


def export_csv(
    dataframe: pd.DataFrame,
    file_name: str,
) -> None:
    output_path = config.OUTPUT_DIR / file_name

    dataframe.to_csv(
        output_path,
        index=False,
        encoding=config.CSV_ENCODING,
    )

    print(
        f"Created {file_name}: "
        f"{len(dataframe):,} rows"
    )


def create_data_dictionary(
    datasets: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    descriptions = {
        "categories": "Product category reference data",
        "stores": "Retail store master data",
        "products": "Product master and pricing data",
        "customers": "Customer master data",
        "sales": "Retail sales transaction line items",
        "returns": "Returned sales transactions",
    }

    rows = []

    for dataset_name, dataframe in datasets.items():
        rows.append(
            {
                "file_name": f"{dataset_name}.csv",
                "description": descriptions[dataset_name],
                "row_count": len(dataframe),
                "column_count": len(dataframe.columns),
                "generated_at": datetime.utcnow().isoformat(),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    ensure_output_directory()

    print(f"Project: {config.PROJECT_NAME}")
    print(f"Company: {config.COMPANY_NAME}")
    print("Generating retail datasets...")

    categories = generate_categories()
    stores = generate_stores()
    products = generate_products(categories)
    customers = generate_customers()

    sales = generate_sales(
        customers=customers,
        products=products,
        stores=stores,
    )

    returns = generate_returns(sales)

    validate_relationships(
        customers=customers,
        products=products,
        stores=stores,
        sales=sales,
        returns=returns,
    )

    datasets = {
        "categories": categories,
        "stores": stores,
        "products": products,
        "customers": customers,
        "sales": sales,
        "returns": returns,
    }

    data_dictionary = create_data_dictionary(datasets)

    for dataset_name, dataframe in datasets.items():
        export_csv(
            dataframe,
            f"{dataset_name}.csv",
        )

    export_csv(
        data_dictionary,
        "data_dictionary.csv",
    )

    print()
    print("Retail data generation completed successfully.")
    print(f"Output directory: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
