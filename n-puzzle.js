let stdin = process.stdin;
const nPuzzle = [1,2,3,4,5,6,7,8,'x'];
const rowNum = 3;
let totalChange = 0;

printPuzzle = () => {
    for(let i=0;i<rowNum;i++){
        let rowQue = '';
        for(let j=0;j<rowNum;j++){
            rowQue = rowQue + '[' + nPuzzle[i*3+j] + ']';
        }
        console.log('%s', rowQue);
    }
}

changePuzzle = (prevNum, toNum) => {
    let popIdx = nPuzzle.indexOf(prevNum);
    let popNum = nPuzzle[popIdx];
    let toIdx = nPuzzle.indexOf(toNum); 
    console.log("change %d to %d", popIdx, toIdx);
    nPuzzle[popIdx] = nPuzzle[toIdx];
    nPuzzle[toIdx] = popNum;
    printPuzzle();
    checkInversion();
}

checkInversion = () => {
    let inversionCnt = 0;
    for (let idx in nPuzzle){
        let checkNum = nPuzzle[idx];
        for(let i=idx;i<nPuzzle.length;i++){
            if( checkNum > nPuzzle[i] ){
                inversionCnt++;
                console.log('(%d , %d)', checkNum, nPuzzle[i]);
            }
        }
    }
    totalChange++;
    console.log('total change: %d', totalChange);
    console.log('total inversion count: %d', inversionCnt);
}
printPuzzle();

let num2 = [];

check2numChange = () => {
    if(num2.length == 2){
        console.log(num2);
        changePuzzle(num2[0], num2[1]);
        num2 = [];
    }
}

// without this, we would only get streams once enter is pressed
//stdin.setRawMode( true );

// resume stdin in the parent process (node app won't quit all by itself
// unless an error or process.exit() happens)
stdin.resume();

// i don't want binary, do you?
stdin.setEncoding( 'utf8' );

// on any data into stdin
stdin.on( 'data', function( key ){
    // ctrl-c ( end of text )
    if ( key === '\u0003' ) {
      process.exit();
    }
    // write the key to stdout all normal like
    num2.push(parseInt(key.trim()));
    check2numChange();
});
