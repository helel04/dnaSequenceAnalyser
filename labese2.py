import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(slots, current_job, decision_text, color_code="\033[0m"):
    print("\n--- Job Sequencing Greedy Algorithm ---")
    print(f"Processing Job {current_job[0]} | Deadline: {current_job[1]} | Profit: {current_job[2]}")
    print(f"Status: {color_code}{decision_text}\033[0m\n")
    
    # Print the timeline / slots
    header = " | ".join([f"Hour {i+1}" for i in range(len(slots))])
    print("      " + header)
    print("      " + "-" * len(header))
    
    row = "      "
    for slot in slots:
        if slot == -1:
            row += " [  ]   "
        else:
            row += f" \033[96m[J{slot}]\033[0m   "
    print(row)
    print("\n" + "="*40 + "\n")

def job_sequencing_visualized(jobs):
    # Sort descending by profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    
    slots = [-1] * max_deadline
    total_profit = 0

    clear_terminal()
    print("Step 1: Jobs sorted descending by profit:")
    for j in jobs:
        print(f"  Job {j[0]}: Profit {j[2]}, Deadline {j[1]}")
    time.sleep(3)

    for job in jobs:
        job_id, deadline, profit = job
        placed = False
        
        # Try to place as close to the deadline as possible
        for i in range(min(max_deadline, deadline) - 1, -1, -1):
            clear_terminal()
            print_status(slots, job, f"Checking Slot {i+1}...", "\033[93m") # Yellow
            time.sleep(1)
            
            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                placed = True
                
                clear_terminal()
                print_status(slots, job, f"SUCCESS! Placed in Slot {i+1}", "\033[92m") # Green
                time.sleep(1.5)
                break
            else:
                clear_terminal()
                print_status(slots, job, f"Slot {i+1} is taken by Job {slots[i]}. Checking previous slot...", "\033[91m") # Red
                time.sleep(1.5)
                
        if not placed:
            clear_terminal()
            print_status(slots, job, "FAILED. No available slots before deadline. Dropping job.", "\033[91m") # Red
            time.sleep(2)

    return slots, total_profit

if __name__ == "__main__":
    jobs = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 1, 30)]
    
    slots, max_profit = job_sequencing_visualized(jobs)
    
    clear_terminal()
    print("="*40)
    print("\033[92mALGORITHM COMPLETE!\033[0m")
    print(f"Final Schedule: {[f'Job {j}' for j in slots if j != -1]}")
    print(f"Total Profit Maximized: {max_profit}")
    print("="*40)