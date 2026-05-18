import pandas as pd

# 1️⃣ الداتا
data = {
    "Order_ID": [1,2,3,4,5,6,7,8,9,10],
    "City": ["Casablanca","Rabat","Casablanca","Marrakech","Rabat","Casablanca","Tangier","Marrakech","Tangier","Casablanca"],
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone","Tablet","Laptop","Phone","Tablet","Laptop"],
    "Quantity": [2,1,3,2,2,1,4,1,3,2],
    "Price": [8000,4000,8000,3000,4000,3000,8000,4000,3000,8000]
}

df = pd.DataFrame(data)

# 2️⃣ إنشاء عمود Total_Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# 3️⃣ مجموع المبيعات كاملين
total_sales = df["Total_Sales"].sum()
print("Total Sales:", total_sales)

# 4️⃣ المدينة لي دارت أكبر مبيعات
top_city = df.groupby("City")["Total_Sales"].sum().idxmax()
print("City with highest sales:", top_city)

# 5️⃣ أكثر منتج مبيعا بالكمية
top_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Most sold product:", top_product)

# 6️⃣ فلترة الطلبات لي Total_Sales > 10000
high_sales_orders = df[df["Total_Sales"] > 10000]
print("\nOrders with Total_Sales > 10000:")
print(high_sales_orders)

# 7️⃣ Pivot Table
pivot = pd.pivot_table(df,
                       values="Total_Sales",
                       index="City",
                       columns="Product",
                       aggfunc="sum")
print("\nPivot Table:")
print(pivot)

# 8️⃣ التحليل النهائي
print("\nAnalysis Report:")
print(f"- Focus marketing on: {top_city}")
print(f"- Best-selling product: {top_product}")