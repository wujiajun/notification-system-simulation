def main() -> None:
    print("\nWelcome to notification system simulation.")

    # Part E code goes here

    # Define permissions
    permissions: list[str] = [
        "receive_calls",
        "receive_messages",
        "review_posts",
    ]
    print(f"\nLoaded {len(permissions)} Permissions: {', '.join(permissions)}")

    # Define notifications
    notifications = {
        "N001": {
            "id": "N001",
            "type": "incoming_call",
            "required_permission": "receive_calls",
            "allowed_roles": ["viewer", "editor", "admin"],
            "allowed_subscriptions": ["basic", "premium"],
        },
        "N002": {
            "id": "N002",
            "type": "missed_call",
            "required_permission": "receive_calls",
            "allowed_roles": ["viewer", "editor", "admin"],
            "allowed_subscriptions": ["basic", "premium"],
        },
        "N003": {
            "id": "N003",
            "type": "message",
            "required_permission": "receive_messages",
            "allowed_roles": ["viewer", "editor", "admin"],
            "allowed_subscriptions": ["basic", "premium"],
        },
        "N004": {
            "id": "N004",
            "type": "post_review",
            "required_permission": "review_posts",
            "allowed_roles": ["editor", "admin"],
            "allowed_subscriptions": ["basic", "premium"],
        },
        "N005": {
            "id": "N005",
            "type": "promotion",
            "required_permission": None,
            "allowed_roles": ["viewer", "editor", "admin"],
            "allowed_subscriptions": ["premium"],
        },
        "N006": {
            "id": "N006",
            "type": "system_alert",
            "required_permission": None,
            "allowed_roles": ["admin"],
            "allowed_subscriptions": ["basic", "premium"],
        },
    }
    print(f"\nLoaded {len(notifications)} notifications.")

    for value in notifications.values():
        print(
            f"id: {value['id']} | "
            f"type: {value['type']} | "
            f"permission: {value['required_permission'] or 'none'} | "
            f"roles: {', '.join(value['allowed_roles'])} | "
            f"subscriptions: {', '.join(value['allowed_subscriptions'])}"
        )

    # Initialize users
    users: list[dict] = [
        {
            "username": "Alice",
            "role": "admin",
            "subscription": "premium",
            "permissions": ["receive_calls", "receive_messages", "review_posts"],
            "is_active": True,
            "is_logged_in": True,
        },
        {
            "username": "Bob",
            "role": "editor",
            "subscription": "premium",
            "permissions": ["receive_calls", "receive_messages", "review_posts"],
            "is_active": True,
            "is_logged_in": False,
        },
        {
            "username": "Charlie",
            "role": "viewer",
            "subscription": "basic",
            "permissions": ["receive_calls", "receive_messages"],
            "is_active": True,
            "is_logged_in": True,
        },
        {
            "username": "Diana",
            "role": "viewer",
            "subscription": "premium",
            "permissions": ["receive_messages"],
            "is_active": True,
            "is_logged_in": False,
        },
        {
            "username": "Ethan",
            "role": "editor",
            "subscription": "basic",
            "permissions": ["receive_calls", "receive_messages", "review_posts"],
            "is_active": False,
            "is_logged_in": False,
        },
    ]

    print(f"\nLoaded {len(users)} users:")

    for user in users:
        active_status = "active" if user["is_active"] else "inactive"
        login_status = "logged in" if user["is_logged_in"] else "logged out"

        print(
            f"{user['username']} | "
            f"{user['role']} | "
            f"{user['subscription']} | "
            f"{active_status} | "
            f"{login_status} | "
            f"permissions: {', '.join(user['permissions'])}"
        )

    while True:
        # Fetch the input
        notification_id = (
            input(
                "\nEnter a notification ID to start the simulation (or type 'exit' to quit): "
            )
            .strip()
            .upper()
        )
        if notification_id == "EXIT":
            print("Simulation ended.")
            return

        # Get the specific notification
        notification = notifications.get(notification_id)
        if notification is None:
            print("Error: Please enter a valid notification ID from the list above.")
            continue

        notification_type = notification.get("type")
        notification_required_permission = notification.get("required_permission")
        notification_allowed_roles = notification.get("allowed_roles")
        notification_allowed_subscriptions = notification.get("allowed_subscriptions")

        print(f"\n=== Simulating {notification_id} " f"({notification_type}) ===")

        for user in users:
            username = user.get("username")
            user_is_active = user.get("is_active")
            user_permissions = user.get("permissions")
            user_is_logged_in = user.get("is_logged_in")
            user_role = user.get("role")
            user_subscription = user.get("subscription")

            # Skip inactive users
            if user_is_active is not True:
                print(f"[SKIPPED] {username} | Inactive account")
                continue

            # Skip users without the required permission
            if (
                notification_required_permission is not None
                and notification_required_permission not in user_permissions
            ):
                print(
                    f"[SKIPPED] {username} | "
                    f"Missing permission: {notification_required_permission}"
                )
                continue

            # Skip roles that cannot receive this notification type
            if user_role not in notification_allowed_roles:
                print(f"[SKIPPED] {username} | " f"Role not allowed: {user_role}")
                continue

            # Skip subscriptions that cannot receive this notification type
            if user_subscription not in notification_allowed_subscriptions:
                print(
                    f"[SKIPPED] {username} | "
                    f"Subscription not allowed: {user_subscription}"
                )
                continue

            # Skip device delivery when the user is logged out
            if user_is_logged_in:
                # Deliver the notification
                print(f"[DELIVERED] {username} | " f"Stored in app and sent to device")
            else:
                # Eligible notifications are always stored in the application
                print(
                    f"[STORED ONLY] {user.get("username")} | "
                    f"Not sent to device because the user is logged out"
                )

        print("=== Simulation completed ===")


if __name__ == "__main__":
    main()
