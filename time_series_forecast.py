import pandas as pd
from fbprophet import Prophet

# Read in data
df = pd.read_csv("sales_data.csv")

# Create prophet model
model = Prophet()

# Fit model to data
model.fit(df)

# Create future dataframe
future_data = model.make_future_dataframe(periods=365)

# Make predictions
forecast = model.predict(future_data)

# Print forecast dataframe
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])
