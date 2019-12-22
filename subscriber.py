from dashboard.indicators import Indicators_Data

# Report on current indicators data
for indicator in Indicators_Data:
    if indicator.name == "open":
        print(f"Current open tickets: {indicator.value}")
    elif indicator.name == "assigned":
        print(f"Current assigned tickets: {indicator.value}")
    else:
        print(f"Current closed tickets: {indicator.value}")
