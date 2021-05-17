//Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

class Solution {
public:
    double myPow(double x, long int n) {
        double result = 1;
        int sign = 1;
        if(n < 0)
        {
            n = -n;
            sign = -1;
        }
        while(n > 0)
        {
            if (n % 2 == 1)
            {
                result *= x;
            }
            x *= x;
            n /= 2;
        }
        if (sign == -1)
        {
            return 1/result;
        }
        return result;
    }
};
