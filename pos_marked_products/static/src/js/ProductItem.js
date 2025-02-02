odoo.define('pos_marked_products.ProductItem', function(require) {
    'use strict';

    const ProductItem = require('point_of_sale.ProductItem');
    const Registries = require('point_of_sale.Registries');

    const MarkedProductItem = ProductItem => class extends ProductItem {
        get productClasses() {
            const classes = super.productClasses || '';
            if (this.props.product.is_marked) {
                return classes + ' marked-product';
            }
            return classes;
        }
    };

    Registries.Component.extend(ProductItem, MarkedProductItem);
    return MarkedProductItem;
});