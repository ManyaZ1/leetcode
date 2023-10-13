class Solution:
    def pancakeSort(self, arr):
        arr_sorted = sorted(arr, reverse = True)

        k_list = []
        for maxi in arr_sorted:
            k = arr.index(maxi) + 1 #max index+1
            k_list.append(k)

            arr = arr[:k][::-1] + arr[k:] #Αντιστροφή από 0 έως k(άρα, το max είναι στο index 0!)
            arr = arr[::-1] #Ολικό reverse(άρα κάναμε flip με k = lenght(arr). ΠΡΟΣΟΧΗ, όχι του αρχηκού arr, αλλά αυτού στο οποιό δουλεύουμε τώρα). Το max είναι στο index = -1.
            k_list.append(len(arr))
            arr.pop(-1) #Δεν μας νοιάζει πια αυτό το max, άρα δουλεύουμε σε υπολίστα!

        return k_list;


       
if __name__=="__main__":
    arr=[1,4,5,6,7]
    s=Solution()
    k=s.pancakeSort(arr)
    print(k)

