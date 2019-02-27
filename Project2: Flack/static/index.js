<script>
  var socket = io.connect( 'http://' + document.domain + ':' + location.port )
  // broadcast a message
  socket.on( 'connect', function() {
    socket.emit( 'my event',
     { data: 'User Connected'
   } )
 })
    var form = $( 'form' ).on( 'submit', function( e ) {
      e.preventDefault()
      var user_name = $( 'input.username' ).val()
      let message = $( 'input.message' ).val()
      console.log(user_name,message)
      // emit the message to webserver.
      
      socket.emit( 'my event', {
        user : user_name,
        msg : message
      } )
      // empty the input field
      $( 'input.message' ).val( '' ).focus()
    } )
  // capture message
  socket.on( 'my response', function( msg ) {
    if( typeof msg.user !== 'undefined' ) {
        $( 'h1' ).remove()
        $( 'div.message_holder' ).append( '<div class="msg_bbl"><b style="color: #000">'+msg.user+'</b> '+msg.msg+'</div>' )
      }
    console.log( msg )
  } )
</script>
