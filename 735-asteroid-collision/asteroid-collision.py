def pon(x,y):
    if (x < 0  and y < 0) or (x > 0  and y > 0):
        return True
    return False


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        
        for i in asteroids:
    
            if st == [] or pon(st[-1], i):
                    st.append(i)
                    
            else:
                while st!=[] and not pon(st[-1],i) and not (st[-1] < 0 and i > 0) and abs(st[-1]) < abs(i):
                        st.pop()
                

                if st== [] or pon(st[-1] , i):
                    st.append(i)
                else:
                    if (st[-1] < 0 and i > 0):
                        st.append(i)
                    else:
                        if abs(st[-1]) == abs(i):
                            st.pop()
               


        return st
                    

                
                
            


                    
