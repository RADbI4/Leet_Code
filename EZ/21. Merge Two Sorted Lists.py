# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        k = 0
        j = 0

        while len(nums1) > m and nums1[-1] == 0:
            nums1.pop(-1)
        while len(nums2) > n and nums2[-1] == 0:
            nums2.pop(-1)

        while i < len(nums1) and k < len(nums2):
            print(nums1[i], nums2[k])
            if nums1[i] < nums2[k]:
                i += 1
                j += 1
            else:
                nums1.insert(j, nums2[k])
                k += 1
                # j += 1
        while (i < m + n) and (len(nums1) < n + m):
            nums1.insert(j, nums2[k])
            i += 1
            k += 1
            j += 1
        while (k < m + n) and (len(nums1) < n + m):
            nums1.insert(j, nums2[k])
            k += 1
            j += 1

if __name__ == "__main__":
    list1 = []
    list2 = []
    sol = Solution()
    list1 = ListNode(val=-100)
    print(list1.val)
    # print(sol.mergeTwoLists(list1, list2))