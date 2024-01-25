// Write an algorithm to determine if a number n is happy.
// A happy number is a number defined by the following process:
//     Starting with any positive integer, replace the number by the sum of the squares of its digits.
//     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
//     Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

// Example 1:
// Input: n = 19
// Output: true
// Explanation:
// 1^2 + 9^2 = 82
// 8^2 + 2^2 = 68
// 6^2 + 8^2 = 100
// 1^2 + 0^2 + 0^2 = 1

#include <iostream>
#include <set>
#include <string>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
      set<string> seen; // Declares the set
      string current = to_string(n); // Converts Int to String

      while (seen.find(current) == seen.end()) {
        seen.insert(current); // Inserts current number to set
        int sum = 0;
        for (char digit : current) { // Rotates through the digits of the current number
          digit = digit - '0'; // Converts String to Int
          sum += digit * digit; // Squares the digit to make
        }

        if (sum == 1) return true;
        current = to_string(sum); // Assigns the new current value to the last sum value
      }
      return false;
    }
};