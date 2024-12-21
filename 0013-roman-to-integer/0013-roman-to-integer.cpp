class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.at(i) == 'I') {
                if (i+1 < s.length() && (s.at(i+1) == 'V' || s.at(i+1) == 'X')) {
                    sum -= 1;
                }
                else  {
                    sum += 1;
                }
            }
            else if (s.at(i) == 'V') {
                sum += 5;
            }
            else if (s.at(i) == 'X') {
                if (i+1 < s.length() && (s.at(i+1) == 'L' || s.at(i+1) == 'C')) {
                    sum -= 10;
                }
                else {
                    sum += 10;
                }
            }
            else if (s.at(i) == 'L') {
                sum += 50;
            }
            else if (s.at(i) == 'C') {
                if (i+1<s.length() && (s.at(i+1) == 'D' || s.at(i+1) == 'M')) {
                    sum -= 100;
                }
                else {
                    sum += 100;
                }
            }
            else if (s.at(i) == 'D') {
                sum += 500;
            }
            else {
                sum += 1000;
            }
        }
        return sum;
    }
};