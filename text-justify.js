/*

brainstorm:
convert string to array using split

check to see if string will fit in one line
  return line

take elements from beginning of string until the resulting joined array is greater than the length
determine the extra spaces needed by subtracting the calculated single spaced length from the desired line length
find the remainder when dividing the number of spaces by the extra spaces
find the quotient when dividing the number of spaces by the extra spaces

join the array with a number of spaces equal to the quotient
add 1 space after the first <remainder> words

*/

var justify = function (str, len) {
  // Your code goes here
  if (str.length <= len) {
    return str;
  } else {
    let strArr = str.split(' ');
    let line = [];
    let wordLen = 0;
    let spaces = 0;

    while (wordLen + spaces <= len && strArr.length > 0) {
      let nextWord = strArr.shift();
      line.push(nextWord);
      wordLen += nextWord.length;
      spaces = line.length - 1;
    }

    if (wordLen + spaces > len) {
      const extraWord = line.pop();
      strArr.unshift(extraWord);
      wordLen -= extraWord.length;
      spaces--;
    }

    const padding = spaces > 0 ? len - wordLen - spaces : 0;
    let lineSpacing = padding > spaces ? Math.floor(spaces / padding) : 1;
    let remainder = padding > spaces ? padding - lineSpacing * spaces : padding;
    let justifiedSpace = ' '.repeat(lineSpacing);

    let counter = 0;
    while (remainder > 0) {
      line[counter] += ' ';
      remainder--;
      counter++;
      if (counter > line.length - 2) {
        counter = 0;
      }
    }

    str = strArr.join(' ');
    return line.join(' ') + '\n' + justify(str, len);
  }
};

// Testing area
console.log(justify('Lorem ipsum dolor sit amet, dolorum fastidii pri ut, cu regione conclusionemque per. Cu integre propriae eam. Ne usu quem aeque ridens, facer novum similique has cu. Nullam senserit tractatos vis ut, eu dicta prompta diceret vel, eu sea veri rebum elitr.', 20));