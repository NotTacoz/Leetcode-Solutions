function createHelloWorld(){
    return function(){
        return ("Hello World");
}
}
;

const f = createHelloWorld();
f();