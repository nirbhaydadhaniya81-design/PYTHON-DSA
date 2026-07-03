# Merge Two Sorted Lists

def merge_waitlist(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            merged.append(list1[i])
            i = i + 1
        else:
            merged.append(list2[j])
            j = j + 1

    while i < len(list1):
        merged.append(list1[i])
        i = i + 1

    while j < len(list2):
        merged.append(list2[j])
        j = j + 1

    return merged


mobile_waitlist = [2, 5, 8, 12]
counter_waitlist = [1, 4, 7, 10]

final_waitlist = merge_waitlist(mobile_waitlist, counter_waitlist)

print("Merged Waitlist:")
print(final_waitlist)