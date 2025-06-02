class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Initialize pointers for string and pattern
        s_ptr, p_ptr = 0, 0
        # Keep track of last '*' position and corresponding string position
        star_ptr, s_tmp = -1, -1
        
        # Process characters while we haven't reached end of string
        while s_ptr < len(s):
            # If pattern pointer is within bounds and characters match or pattern has '?'
            if p_ptr < len(p) and (p[p_ptr] == '?' or s[s_ptr] == p[p_ptr]):
                s_ptr += 1
                p_ptr += 1
            # If we encounter a '*'
            elif p_ptr < len(p) and p[p_ptr] == '*':
                # Store star position and current string position
                star_ptr = p_ptr
                s_tmp = s_ptr
                p_ptr += 1
            # If we have a previous star to fall back to
            elif star_ptr != -1:
                # Backtrack: try matching '*' with one more character
                p_ptr = star_ptr + 1
                s_tmp += 1
                s_ptr = s_tmp
            else:
                return False
        
        # Check if remaining pattern characters are all '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)