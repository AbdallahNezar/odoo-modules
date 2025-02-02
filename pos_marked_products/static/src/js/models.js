odoo.define('pos_marked_products.models', function(require) {
    'use strict';
    
    const { PosGlobalState } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const PosMarkedProductsGlobalState = PosGlobalState => class extends PosGlobalState {
        async load_server_data() {
            const result = await super.load_server_data();
            
            try {
                const products = await this.env.services.rpc({
                    model: 'product.product',
                    method: 'search_read',
                    domain: [['available_in_pos', '=', true]],
                    fields: ['id', 'is_marked'],
                });

                if (products && products.length > 0) {
                    products.forEach(product => {
                        const posProduct = this.db.product_by_id[product.id];
                        if (posProduct) {
                            posProduct.is_marked = product.is_marked;
                        }
                    });
                }
            } catch (error) {
                console.error('Error loading marked products:', error);
            }

            return result;
        }
    };

    Registries.Model.extend(PosGlobalState, PosMarkedProductsGlobalState);
});