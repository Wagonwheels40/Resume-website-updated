const tree = {
    title: 'A'
    'children': [
        {
            title: 'B'
            'children': [
                {
                    title: 'C'
                }
            ]
        },
        {
            title: 'D'
        }
    ]
}

function start(node){ i = 6
    console.log('Node:', node.title); debugger;
    if(node.children){
        node.children.forEach(function(child){
            start(child);
        }) 
    }
}

start(tree);