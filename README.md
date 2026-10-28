# Notification System Simulation

A small Python command-line program that simulates a notification system.
You choose a notification, and the program shows which users receive it and why other users do not.

This is a student project for the course CMPS-3000 (Computational Thinking and Problem Solving) at SAIT.

## What It Does

The program has 6 notifications and 5 sample users. All data is kept in memory, and nothing is saved when the program closes.

For each notification, the program checks every user in this order:

1. **Account status.** The account must be active.
2. **Permission.** The user must have the permission that the notification needs (if it needs one).
3. **Role.** The user's role must be allowed for this notification.
4. **Subscription.** The user's subscription (basic or premium) must be allowed.
5. **Login status.** If all checks pass, the notification is stored in the app. It is also sent to the device only if the user is logged in.

The first check that fails decides the result, and the program shows the reason.

## Result Labels

| Label | Meaning |
| --- | --- |
| `[DELIVERED]` | The user is logged in. The notification is stored in the app and sent to the device. |
| `[STORED ONLY]` | The user is logged out. The notification is stored in the app but not sent to the device. |
| `[SKIPPED]` | The user does not get the notification. The reason is shown. |

## Sample Data

### Notifications

| ID | Type | Required permission | Allowed roles | Allowed subscriptions |
| --- | --- | --- | --- | --- |
| N001 | incoming_call | receive_calls | viewer, editor, admin | basic, premium |
| N002 | missed_call | receive_calls | viewer, editor, admin | basic, premium |
| N003 | message | receive_messages | viewer, editor, admin | basic, premium |
| N004 | post_review | review_posts | editor, admin | basic, premium |
| N005 | promotion | none | viewer, editor, admin | premium |
| N006 | system_alert | none | admin | basic, premium |

### Users

| Username | Role | Subscription | Account | Login | Permissions |
| --- | --- | --- | --- | --- | --- |
| Alice | admin | premium | active | logged in | receive_calls, receive_messages, review_posts |
| Bob | editor | premium | active | logged out | receive_calls, receive_messages, review_posts |
| Charlie | viewer | basic | active | logged in | receive_calls, receive_messages |
| Diana | viewer | premium | active | logged out | receive_messages |
| Ethan | editor | basic | inactive | logged out | receive_calls, receive_messages, review_posts |

## Requirements

- Python 3.12 or newer
- No other packages are needed
- [uv](https://docs.astral.sh/uv/) is optional (used to manage the project)

## How to Run

With uv, run this in the project folder:

```bash
uv run notification-system-simulation
```

Without uv, go into the `src` folder and run:

```bash
python3 -m notification_system_simulation.main
```

## How to Use

1. Start the program. It prints the permissions, notifications and users.
2. Type a notification ID, for example `N004`, and press Enter.
3. Read the result for each user.
4. Type another ID to try again, or type `exit` to quit.

IDs are not case sensitive, so `n004` also works. An unknown ID shows an error message and asks again.

## Example

Input: `N004` (post_review)

| User | Result | Why |
| --- | --- | --- |
| Alice | DELIVERED | Has the permission, is an admin, and is logged in |
| Bob | STORED ONLY | Passes all checks, but is logged out |
| Charlie | SKIPPED | Missing permission: review_posts |
| Diana | SKIPPED | Missing permission: review_posts |
| Ethan | SKIPPED | Inactive account |

## Project Structure

```
notification-system-simulation/
├── pyproject.toml
├── README.md
└── src/
    └── notification_system_simulation/
        ├── __init__.py
        └── main.py        # all the simulation logic
```

## Notes

- This is a simulation only. It does not send real notifications.
- Users and notifications are written directly in `main.py`. To try other cases, edit the data there.