# Order Fulfillment Facade — Starter

Small class activity for the **Facade** pattern.

The client currently coordinates four valid subsystem services directly:

- Inventory
- Payment
- Shipping
- Notification

## Your task

1. Create `OrderFulfillmentFacade.place_order(order)`.
2. Move the common coordination sequence into the Facade.
3. Do **not** modify the subsystem service classes.
4. Keep subsystem responsibilities in their existing classes.
5. Add one focused test proving the client can place an order through the Facade.
6. Be ready to name one complexity cost introduced by the Facade.

Use explicit OO design and keep one main class per source file.

## Team workflow

Only one teammate creates the repository from this template. The team repository must be **public** and everyone works in the same repository.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Design notes

| Role | Class |
| --- | --- |
| Facade | `OrderFulfillmentFacade` |
| Subsystem | `InventoryService`, `PaymentService`, `ShippingService`, `NotificationService` |
| Client | `OrderClient` |

`OrderClient` now depends only on `OrderFulfillmentFacade`. The facade owns the coordination sequence (reserve, charge, ship, notify) and delegates each step to the service that already owned it. No service class was changed, and the facade adds no business rules of its own.

### Complexity cost

The facade is one more class every order goes through, and it hides the order of the steps from the client. If a client needs a different flow (for example, charging before reserving, or skipping the notification) it has to bypass the facade or the facade needs another method, so it can slowly grow into a god object that knows every subsystem. It also concentrates failure handling: today a failed step does not roll back the previous ones, and that is now the facade's problem to solve.
