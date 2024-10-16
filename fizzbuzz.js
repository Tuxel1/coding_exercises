/* Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for the multiples of 
five print “Buzz”. For numbers which are multiples of both three and five print 
“FizzBuzz”. */

for (let i = 1; i <= 100; i++) {
    let output = 
        (i % 5 == 0 && i % 3 == 0) ? "FizzBuzz" :
        (i % 5 == 0) ? "Buzz" :
        (i % 3 == 0) ? "Fizz" :
        i;
    
    console.log(output);
}