import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

import time
from bot.orders import execute_trade, get_order_status
from bot.validators import validate_side, validate_order_type, validate_quantity

app = typer.Typer(help="binance futures testnet bot")
console = Console()

@app.command()
def trade(
    symbol: str = typer.Argument(None, help="Trading symbol, e.g. BTCUSDT"),
    side: str = typer.Argument(None, help="BUY or SELL"),
    order_type: str = typer.Argument(None, help="MARKET, LIMIT, or STOP_MARKET"),
    qty: float = typer.Argument(None, help="Quantity to trade"),
    price: float = typer.Option(None, "--price", "-p", help="Order price")
):
    if not symbol:
        symbol = typer.prompt("Enter Symbol (e.g. BTCUSDT)")
    if not side:
        side = typer.prompt("Enter Side (BUY/SELL)")
    if not order_type:
        order_type = typer.prompt("Enter Order Type (MARKET/LIMIT/STOP_MARKET)")
    if not qty:
        qty = typer.prompt("Enter Quantity", type=float)
    if order_type.upper() in ["LIMIT", "STOP_MARKET"] and not price:
        price = typer.prompt("Enter Price", type=float)

    try:
        side_val = validate_side(side)
        type_val = validate_order_type(order_type)
        qty_val = validate_quantity(qty)
    except ValueError as e:
        console.print(f"[bold red]bad input:[/bold red] {e}")
        raise typer.Exit(code=1)

    console.print(Panel(
        f"[bold blue]preparing order[/bold blue]\n"
        f"symbol: {symbol.upper()}\n"
        f"side: {side_val}\n"
        f"type: {type_val}\n"
        f"qty: {qty_val}\n"
        f"price: {price if price else 'none'}",
        expand=False
    ))

    try:
        data = execute_trade(
            symbol=symbol,
            side=side_val,
            type=type_val,
            qty=qty_val,
            price=price
        )
        
        # get fill status update
        order_id = data.get("orderId")
        if order_id:
            time.sleep(0.5)
            updated_data = get_order_status(symbol, order_id)
            if updated_data:
                data = updated_data
        
        table = Table(title="[bold green]order success[/bold green]")
        table.add_column("field", style="cyan")
        table.add_column("value", style="magenta")

        table.add_row("id", str(data.get("orderId", "N/A")))
        table.add_row("status", str(data.get("status", "N/A")))
        table.add_row("filled qty", str(data.get("executedQty", "N/A")))
        
        avg_price = data.get("avgPrice")
        if avg_price and float(avg_price) > 0:
            table.add_row("avg price", str(avg_price))
        else:
            table.add_row("avg price", "N/A (pending match)")

        console.print(table)
    except Exception as e:
        console.print(Panel(
            f"[bold red]failed:[/bold red]\n{str(e)}",
            expand=False,
            border_style="red"
        ))

if __name__ == "__main__":
    app()
