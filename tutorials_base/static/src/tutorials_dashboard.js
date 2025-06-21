import { Component, useState, onWillStart, markup } from '@odoo/owl';
import { registry } from "@web/core/registry";

import { rpc } from "@web/core/network/rpc";

export class TutorialsDashboard extends Component {
    static template = "tutorials_base.tutorials_dashboard";

    setup(){
        this.state = useState({
            tutorials: [],
            loading: true,
            error: null
        })

        onWillStart(async ()=>{
            let tutorials;

            try {
                tutorials = await rpc("/odoo-tutorials");
            } catch(e){
                this.state.error = "Failed to load tutorials"
            } finally {
                this.state.loading = false;
            }

            if (tutorials){
                tutorials.forEach(function(tutorial){
                    tutorial.title = markup(tutorial.title);
                });
                this.state.tutorials = tutorials;
            }
        })
    }
}

registry.category("actions").add("tutorials_base.tutorials_dashboard", TutorialsDashboard)