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
    nums1 = [-1, 20]
    m = 2
    nums2 = [1, 2, 3, 4, 50, 0, 0, 0, 0, 0]
    n = 5
    Solution.merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)
