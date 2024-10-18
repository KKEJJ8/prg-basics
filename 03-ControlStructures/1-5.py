# Total number of tasks in the test
total_tasks = 20

# List of properly performed tasks to check
tasks_ok_list = [20, 11, 10, 9, 0]

# Process each test case
for tasks_ok in tasks_ok_list:
    test_passed = False

    # Check if at least 50% of the tasks were performed correctly
    if tasks_ok >= total_tasks * 0.5:
        test_passed = True

    # Output the result for each test
    if test_passed:
        print(f"With {tasks_ok} tasks correct: Congratulations! You passed the test.")
    else:
        print(f"With {tasks_ok} tasks correct: Unfortunately, you failed the test.")