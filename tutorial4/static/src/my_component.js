import { Component } from '@odoo/owl';
import { registry } from "@web/core/registry";


export class YourOwlComponentName extends Component {
    static template = "your_component_template_name";

    setup(){
        this.variable1 = this.props.action.params.variable1;
    }
}

registry.category("actions").add("custom_client_action_name", YourOwlComponentName)