import os
import pandas as pd

# =====================================================
# Current Working Directory
# =====================================================

print("===== CURRENT WORKING DIRECTORY =====")

print(os.getcwd())


# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv(
    'data/superstore.csv',
    encoding='latin1'
)


# =====================================================
# First 5 Rows
# =====================================================

print("\n===== FIRST 5 ROWS =====")

print(df.head())


# =====================================================
# Dataset Shape
# =====================================================

print("\n===== DATASET SHAPE =====")

print(df.shape)


# =====================================================
# Column Names
# =====================================================

print("\n===== COLUMN NAMES =====")

print(df.columns)


# =====================================================
# Missing Values
# =====================================================

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())


# =====================================================
# Statistical Summary
# =====================================================

print("\n===== STATISTICAL SUMMARY =====")

print(df.describe())


# =====================================================
# Sales by Category
# =====================================================

print("\n===== SALES BY CATEGORY =====")

print(
    df.groupby('Category')['Sales']
      .sum()
      .sort_values(ascending=False)
)


# =====================================================
# Profit by Category
# =====================================================

print("\n===== PROFIT BY CATEGORY =====")

print(
    df.groupby('Category')['Profit']
      .sum()
      .sort_values(ascending=False)
)


# =====================================================
# Correlation Matrix
# =====================================================

print("\n===== CORRELATION MATRIX =====")

correlation = df[
    ['Sales', 'Profit', 'Discount', 'Quantity']
].corr()

print(correlation)