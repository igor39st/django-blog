CKEDITOR.replace( 'article', {
            toolbar: [
                { name: 'basicstyles', items: [ 'Bold', 'Italic' ] },
                { name: 'paragraph', items : [ 'NumberedList','BulletedList','-','Blockquote' ] },
                { name: 'links', items : [ 'Link','Unlink' ] },
                { name: 'insert', items : [ 'Image' ] }
            ],
            uiColor: '#f9fafb',
            height: '100%'
        });