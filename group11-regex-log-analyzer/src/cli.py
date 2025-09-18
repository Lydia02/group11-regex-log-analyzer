# Count errors/warnings from filtered entries only
        errors, warnings = temp_analyzer.count_errors_warnings()
        print(f"Errors: {errors}, Warnings: {warnings}")

        # Get top endpoints from filtered entries only
        top_eps = temp_analyzer.top_endpoints()
        print("Top Endpoints:")
        for ep, count in top_eps:
            print(f"{ep}: {count}")

        # Get top IPs from filtered entries only
        top_ips = temp_analyzer.top_ips()
        print("Top IP Addresses:")
        for ip, count in top_ips:
            print(f"{ip}: {count}")
            
    except ValueError as ve:
        print(ve)

if _name_ == "_main_":
    main()
