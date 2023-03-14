const confirmarPedido = document.getElementById('pedidoauuu');

// Deshabilita el botón "Confirmar pedido" inicialmente
confirmarPedido.disabled = true;
  function initPayPalButton() 
  {
    paypal.Buttons({
      style: {
        shape: 'rect',
        color: 'gold',
        layout: 'vertical',
        label: 'paypal',

      },

      createOrder: function(data, actions) {
        return actions.order.create({
          purchase_units: [{
            amount:{
            value: '{{orden.total}}'
        }
    }]
        });
      },

      onApprove: function(data, actions) {
          return actions.order.capture().then(function(orderData) {

            // Full available details
            console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

            // Show a success message within this page, e.g.
            const element = document.getElementById('paypal-button-container');
            element.innerHTML = '';
            element.innerHTML = '<h3>Thank you for your payment!</h3>';
            // Or go to another URL:  actions.redirect('thank_you.html');
                    // Habilita el botón "Confirmar pedido"
            confirmarPedido.disabled = false;
          });
        },

        onError: function(err) {
          console.log(err);
        }
      }).render('#paypal-button-container');
    }
    initPayPalButton();