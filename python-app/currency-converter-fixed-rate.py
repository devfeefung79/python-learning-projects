from typing import Dict


class CurrencyConversionError(Exception):
    """Custom exception for currency conversion errors."""


class FixedRateCurrencyConverter:
    """
    Currency converter using fixed exchange rates relative to USD.
    """

    def __init__(self, rates: Dict[str, float], base_currency: str = "USD") -> None:
        self.rates = {k.upper(): v for k, v in rates.items()}
        self.base_currency = base_currency.upper()

        if self.base_currency not in self.rates:
            raise CurrencyConversionError(f"Unsupported base currency: {self.base_currency}")

    def convert(self, amount: float, target_currency: str) -> float:
        """
        Convert amount from base_currency to target_currency.

        Args:
            amount (float): The amount of money to convert.
            target_currency (str): Currency code to convert to.

        Returns:
            float: Converted amount.

        Raises:
            CurrencyConversionError: If target_currency is unsupported.
        """
        target_currency = target_currency.upper()

        if target_currency not in self.rates:
            raise CurrencyConversionError(f"Unsupported target currency: {target_currency}")

        # Normalize amount to USD
        amount_in_usd = amount / self.rates[self.base_currency]

        # Convert from USD to target currency
        return amount_in_usd * self.rates[target_currency]


def get_user_input(prompt: str) -> str:
    """Get non-empty user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_float(prompt: str) -> float:
    """Get a positive float from user input."""
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid number. Please enter a valid amount.")


def main():
    RATES = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0,
        "GBP": 0.75,
        "AUD": 1.35,
    }

    converter = FixedRateCurrencyConverter(rates=RATES, base_currency="USD")

    print("=== Fixed Rate Currency Converter ===")

    amount = get_positive_float("Enter amount in USD: ")
    target_currency = get_user_input("Enter target currency code (e.g., EUR, JPY, GBP): ").upper()

    try:
        converted_amount = converter.convert(amount, target_currency)
    except CurrencyConversionError as e:
        print(f"Conversion error: {e}")
        return

    print(f"{amount:.2f} {converter.base_currency} = {converted_amount:.2f} {target_currency}")


if __name__ == "__main__":
    main()
