(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-299c41f4"],{"2a9d":function(t,e,a){},5695:function(t,e,a){"use strict";var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"table-page-search-wrapper"},[a("form-validate",{attrs:{layout:"inline",form:t.queryParam}},[a("a-row",{attrs:{gutter:24}},[a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"ID"}},[a("a-input",{on:{pressEnter:function(){return t.$refs.tableList.refresh()}},model:{value:t.queryParam.id,callback:function(e){t.$set(t.queryParam,"id",e)},expression:"queryParam.id"}})],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Booking ID"}},[a("a-input",{on:{pressEnter:function(){return t.$refs.tableList.refresh()}},model:{value:t.queryParam.booking_id,callback:function(e){t.$set(t.queryParam,"booking_id",e)},expression:"queryParam.booking_id"}})],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Ticket ID"}},[a("a-input",{on:{pressEnter:function(){return t.$refs.tableList.refresh()}},model:{value:t.queryParam.ticket_id,callback:function(e){t.$set(t.queryParam,"ticket_id",e)},expression:"queryParam.ticket_id"}})],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Create"}},[a("a-range-picker",{on:{change:function(){return t.$refs.tableList.refresh()}},model:{value:t.date,callback:function(e){t.date=e},expression:"date"}})],1)],1),a("a-col",{attrs:{md:24,sm:24}},[a("form-item-validate",[a("a-input-search",{attrs:{placeholder:"E.g Serial No. or Email or Name or Passport","enter-button":"Search"},on:{search:function(){return t.$refs.tableList.refresh()}},model:{value:t.queryParam.search,callback:function(e){t.$set(t.queryParam,"search",e)},expression:"queryParam.search"}})],1)],1)],1)],1),a("s-table",{ref:"tableList",attrs:{size:"default",rowKey:function(t){return t.id},columns:t.columns,data:t.loadData,showPagination:"auto",pageURI:!0,rowSelection:t.rowSelection,bordered:"",scroll:{x:1200}},scopedSlots:t._u([{key:"is_lock",fn:function(t){return[a("a-checkbox",{attrs:{checked:t,disabled:""}})]}},{key:"action",fn:function(e){return null==t.rowSelection?[e.booking_id?a("router-link",{directives:[{name:"action",rawName:"v-action:view_ticket",arg:"view_ticket"}],attrs:{to:{name:"BookingDetail",params:{id:e.booking_id}}}},[a("span",[t._v("Booking")])]):a("span",[t._v("Booking")]),a("a-divider"),e.ticket_id?a("router-link",{directives:[{name:"action",rawName:"v-action:view_ticket",arg:"view_ticket"}],attrs:{to:{name:"TicketDetail",params:{id:e.ticket_id}}}},[a("span",[t._v("Ticket")])]):a("span",[t._v("Ticket")])]:void 0}}],null,!0)})],1)},r=[],n=a("2af9"),o=a("9b6f"),s=a("c1df"),l=a.n(s),c={components:{STable:n["d"],FormValidate:n["c"],FormItemValidate:n["b"]},props:{rowSelection:{type:Object,default:null}},methods:{},data:function(){var t=this;return{date:[],queryParam:{name:void 0},columns:[{title:"ID",dataIndex:"id",align:"center",width:"80px",sorter:!0},{title:"Serial No",dataIndex:"serial_no",align:"center",width:"160px"},{title:"Email",dataIndex:"email",align:"center",width:"180px",ellipsis:!0},{title:"Name",dataIndex:"name",align:"center",width:"160px",ellipsis:!0},{title:"Passport No",dataIndex:"passport_no",align:"center",width:"160px",ellipsis:!0},{title:"Travel Plan",align:"center",children:[{title:"Entry",dataIndex:"entry",align:"center",ellipsis:!0},{title:"Exit",dataIndex:"exit",align:"center",ellipsis:!0}]},{title:"Quotation",align:"center",children:[{title:"Ticket1",dataIndex:"ticket1",align:"center",ellipsis:!0},{title:"Ticket2",dataIndex:"ticket2",align:"center",ellipsis:!0}]},{title:"Hotel",dataIndex:"hotel",align:"center",ellipsis:!0},{title:"Remark",dataIndex:"remark",align:"center",ellipsis:!0},{title:"Lock",dataIndex:"is_lock",align:"center",width:"80px",ellipsis:!0,scopedSlots:{customRender:"is_lock"}},{title:"Author",dataIndex:"author",align:"center",ellipsis:!0},{title:"Create",dataIndex:"date",align:"center",ellipsis:!0},{title:"Action",align:"center",scopedSlots:{customRender:"action"}}],loadData:function(e){return Object(o["c"])(Object.assign(e,Object.assign({date_before:null!=t.date&&t.date.length>0?l()(t.date[1]).format("YYYY-MM-DD"):void 0,date_after:null!=t.date&&t.date.length>0?l()(t.date[0]).format("YYYY-MM-DD"):void 0},t.queryParam))).then((function(e){var a=e.result.data;return t.$emit("onData",a.data),a}))}}}},d=c,u=a("2877"),m=Object(u["a"])(d,i,r,!1,null,null,null);e["a"]=m.exports},"59ce":function(t,e,a){"use strict";a.d(e,"e",(function(){return n})),a.d(e,"c",(function(){return o})),a.d(e,"a",(function(){return s})),a.d(e,"f",(function(){return l})),a.d(e,"b",(function(){return c})),a.d(e,"d",(function(){return d}));var i=a("365c"),r=a("b775");function n(t){return Object(r["b"])({url:i["a"].Ticket,method:"get",params:t})}function o(t,e){return Object(r["b"])({url:i["a"].Ticket+"".concat(t,"/"),params:e,method:"get"})}function s(t){return Object(r["b"])({url:i["a"].Ticket,method:"post",data:t}).then(i["e"]).catch(i["d"])}function l(t,e){return Object(r["b"])({url:i["a"].Ticket+"".concat(t,"/"),method:"patch",data:e}).then(i["i"]).catch(i["h"])}function c(t,e){return Object(r["b"])({url:i["a"].Ticket+"".concat(t,"/"),method:"delete"}).then(i["g"]).catch(i["f"])}function d(t){return Object(r["b"])({url:i["a"].TicketHistory,method:"get",params:t})}},6991:function(t,e,a){"use strict";var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("form-validate",{ref:"observer",attrs:{form:t.form}},[a("page-header-wrapper",{attrs:{content:"ID:"+t.$route.params.id}},["edit"==t.post_type?a("a-card",{staticClass:"card",attrs:{title:"Progress",bordered:!1}},[t.form.is_cancel?a("a-steps",{attrs:{direction:t.isMobile?"vertical":"horizontal",current:1,progressDot:""}},[a("a-step",{scopedSlots:t._u([{key:"title",fn:function(){return[a("span",[t._v("Create Ticket")])]},proxy:!0},{key:"description",fn:function(){return[a("div",{staticClass:"antd-pro-pages-profile-advanced-style-stepDescription"},[t._v(" "+t._s(t.form.author)+" "),a("div",[t._v(t._s(t.form.date))])])]},proxy:!0}],null,!1,2317930995)}),a("a-step",{attrs:{title:"Cancelled"}})],1):a("a-steps",{attrs:{direction:t.isMobile?"vertical":"horizontal",current:t.current,progressDot:""}},[a("a-step",{scopedSlots:t._u([{key:"title",fn:function(){return[a("span",[t._v("Create Ticket")])]},proxy:!0},{key:"description",fn:function(){return[a("div",{staticClass:"antd-pro-pages-profile-advanced-style-stepDescription"},[t._v(" "+t._s(t.form.author)+" "),a("div",[t._v(t._s(t.form.date))])])]},proxy:!0}],null,!1,2317930995)}),a("a-step",{attrs:{title:"Booked"}}),a("a-step",{attrs:{title:"Confirmed"}}),a("a-step",{attrs:{title:"Completed"}})],1)],1):t._e(),a("a-card",{staticClass:"card",attrs:{title:"Ticket Info",bordered:!1}},[a("a-row",{staticClass:"form-row",attrs:{gutter:16}},[a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Serial No.",vid:"serial_no"}},[a("a-input",{attrs:{disabled:t.disabled()},model:{value:t.form.serial_no,callback:function(e){t.$set(t.form,"serial_no",e)},expression:"form.serial_no"}})],1)],1),a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Line",vid:"air_line"}},[a("a-input",{attrs:{disabled:t.disabled()},model:{value:t.form.air_line,callback:function(e){t.$set(t.form,"air_line",e)},expression:"form.air_line"}})],1)],1),a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Class",vid:"air_class"}},[a("a-input",{attrs:{disabled:t.disabled()},model:{value:t.form.air_class,callback:function(e){t.$set(t.form,"air_class",e)},expression:"form.air_class"}})],1)],1),a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Fare",vid:"fare"}},[a("a-input-number",{staticClass:"w-full",attrs:{disabled:t.disabled(),min:0,precision:2,decimalSeparator:"."},model:{value:t.form.fare,callback:function(e){t.$set(t.form,"fare",e)},expression:"form.fare"}})],1)],1),a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Tax",vid:"tax"}},[a("a-input-number",{staticClass:"w-full",attrs:{disabled:t.disabled(),min:0,precision:2,decimalSeparator:"."},model:{value:t.form.tax,callback:function(e){t.$set(t.form,"tax",e)},expression:"form.tax"}})],1)],1),a("a-col",{attrs:{sm:24,md:8}},[a("form-item-validate",{attrs:{label:"Total",vid:"total"}},[a("a-input-number",{staticClass:"w-full",attrs:{disabled:t.disabled(),min:0,precision:2,decimalSeparator:"."},model:{value:t.form.total,callback:function(e){t.$set(t.form,"total",e)},expression:"form.total"}})],1)],1),a("a-col",{attrs:{sm:24,md:12}},[a("form-item-validate",{attrs:{label:"Info",vid:"air_info"}},[a("a-textarea",{attrs:{disabled:t.disabled(),rows:5},model:{value:t.form.air_info,callback:function(e){t.$set(t.form,"air_info",e)},expression:"form.air_info"}})],1)],1),a("a-col",{attrs:{sm:24,md:12}},[a("form-item-validate",{attrs:{label:"remark",vid:"remark"}},[a("a-textarea",{attrs:{disabled:t.disabled(),rows:5},model:{value:t.form.remark,callback:function(e){t.$set(t.form,"remark",e)},expression:"form.remark"}})],1)],1)],1),"edit"==t.post_type&&t.form.uploads?a("a-upload-dragger",{attrs:{multiple:!0,"before-upload":t.beforeUpload,remove:t.handleRemove,action:"http://localhost:8001/api/uploads/",withCredentials:!0,"default-file-list":t.form.uploads,data:{content_type:"ticket",object_id:t.$route.params.id},disabled:t.disabled()||t.form.is_confirm}},[a("p",{staticClass:"ant-upload-drag-icon"},[a("a-icon",{attrs:{type:"inbox"}})],1),a("p",{staticClass:"ant-upload-text"},[t._v(" Click or drag file to this area to upload ")]),a("p",{staticClass:"ant-upload-hint"},[t._v(" Support for a single or bulk upload ")])]):t._e()],1),a("form-item-validate",{attrs:{vid:"user_id"}},[a("itinerary-related-list",{attrs:{disabled:t.disabled()},on:{select:t.onSelectItinerary}})],1)],1),"edit"==t.post_type?a("a-row",[a("a-col",{attrs:{span:12}},[t.$auth("delete_ticket")?a("a-popconfirm",{attrs:{title:"Are you sure delete?",okText:"Yes",cancelText:"No"},on:{confirm:t.onDelete}},[a("a-button",{attrs:{href:"javascript:;",type:"danger"}},[t._v("Delete")])],1):t._e()],1),a("a-col",{staticClass:"text-right",attrs:{span:12}},["edit"==t.post_type?a("a-button",{directives:[{name:"action",rawName:"v-action:change_ticket",arg:"change_ticket"}],attrs:{type:"primary",loading:t.updateing,"html-type":"submit"},on:{click:t.submit}},[t._v(" Submit ")]):t._e()],1)],1):t._e(),a("a-row",[a("a-col",{staticClass:"text-right",attrs:{span:24}},["add"==t.post_type?a("a-button",{directives:[{name:"action",rawName:"v-action:add_ticket",arg:"add_ticket"}],attrs:{type:"primary",loading:t.updateing,"html-type":"submit"},on:{click:t.submit}},[t._v(" Submit ")]):t._e()],1)],1)],1)},r=[],n=(a("d3b7"),a("ac1f"),a("5319"),a("2af9")),o=a("59ce"),s=a("91b6"),l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a-card",{staticClass:"card",attrs:{title:"Related Itineraries",bordered:!1}},[a("a-table",{ref:"table",attrs:{size:"default",rowKey:function(t){return t.id},columns:t.columns,"data-source":t.data,pagination:!1,loading:t.loading,scroll:{x:1200},bordered:""},scopedSlots:t._u([{key:"is_lock",fn:function(t){return[a("a-checkbox",{attrs:{checked:t,disabled:""}})]}}])}),a("a-button",{staticClass:"text-center w-full h-12 mt-4",attrs:{type:"primary",disabled:t.loading||t.disabled},on:{click:function(){t.modal=!0}}},[t._v("Related Itinerary")]),a("a-modal",{attrs:{title:"Related Itinerary",width:"90%"},model:{value:t.modal,callback:function(e){t.modal=e},expression:"modal"}},[a("template",{slot:"footer"},[a("a-button",{key:"submit",attrs:{type:"primary"},on:{click:t.handleOk}},[t._v(" Select ")])],1),a("itinerary-table-list",{attrs:{rowSelection:{selectedRowKeys:t.selectedRowKeys,onChange:t.onSelectChange,getCheckboxProps:function(e){return{props:{disabled:null!=e.ticket_id&&!t.data.find((function(t){return t.id==e.id}))}}}}},on:{onData:t.onData}})],2)],1)},c=[],d=(a("7db0"),a("d81d"),a("5695")),u=a("9b6f"),m={components:{ItineraryTableList:d["a"]},props:{disabled:{type:Boolean,default:!1}},watch:{data:function(t){this.$emit("select",t.map((function(t){return t.id}))),this.selectedRowKeys=t.map((function(t){return t.id}))}},mounted:function(){this.$route.params.id?this.getData():this.data=Object.assign([],this.$route.params.itinerary)},methods:{getData:function(){var t=this;this.loading=!0,Object(u["c"])({ticket_id:this.$route.params.id}).then((function(e){var a=e.result.data;t.data=Object.assign([],a)})).finally((function(){t.loading=!1}))},handleOk:function(){var t=this,e=this.selectedRowKeys.map((function(e){return t.modalData.find((function(t){return t.id===e}))}));this.modal=!1,this.data=Object.assign([],e)},onData:function(t){this.modalData=Object.assign([],t)},onSelectChange:function(t){this.selectedRowKeys=t}},data:function(){return{loading:!1,data:[],modalData:[],selectedRowKeys:[],modal:!1,queryParam:{name:void 0},columns:[{title:"ID",dataIndex:"id",align:"center",width:"80px",sorter:!0},{title:"Serial No",dataIndex:"serial_no",align:"center",width:"160px"},{title:"Email",dataIndex:"email",align:"center",width:"180px",ellipsis:!0},{title:"Name",dataIndex:"name",align:"center",width:"160px",ellipsis:!0},{title:"Passport No",dataIndex:"passport_no",align:"center",width:"160px",ellipsis:!0},{title:"Travel Plan",align:"center",children:[{title:"Entry",dataIndex:"entry",align:"center",ellipsis:!0},{title:"Exit",dataIndex:"exit",align:"center",ellipsis:!0}]},{title:"Quotation",align:"center",children:[{title:"Ticket1",dataIndex:"ticket1",align:"center",ellipsis:!0},{title:"Ticket2",dataIndex:"ticket2",align:"center",ellipsis:!0}]},{title:"Hotel",dataIndex:"hotel",align:"center",ellipsis:!0},{title:"Remark",dataIndex:"remark",align:"center",ellipsis:!0},{title:"Lock",dataIndex:"is_lock",align:"center",width:"80px",ellipsis:!0,scopedSlots:{customRender:"is_lock"}},{title:"Author",dataIndex:"author",align:"center",ellipsis:!0}]}}},f=m,p=a("2877"),b=Object(p["a"])(f,l,c,!1,null,null,null),h=b.exports,g=(a("c1df"),{components:{FormValidate:n["c"],FormItemValidate:n["b"],ItineraryRelatedList:h},props:{post_type:{type:String,default:"edit"}},data:function(){var t=this;return{loading:!1,updateing:!1,disabled:function(){return("add"!=t.post_type||!t.$auth("add_ticket"))&&("edit"!=t.post_type||!t.$auth("change_ticket"))},form:{},itineraries_id:[]}},mounted:function(){this.$route.params.id&&this.getTicketData()},computed:{current:function(){var t=0;return this.form.is_booking&&(t=1),this.form.is_confirm&&(t=2),this.form.is_complete&&(t=3),t}},methods:{getTicketData:function(){var t=this;this.loading=!0,Object(o["c"])(this.$route.params.id).then((function(e){var a=e.result.data;t.form=Object.assign({},a)})).finally((function(){t.loading=!1}))},submit:function(){var t=this;this.updateing=!0;var e=Object.assign({serial_no:this.form.serial_no,air_line:this.form.air_line,air_class:this.form.air_class,fare:this.form.fare,tax:this.form.tax,total:this.form.total,air_info:this.form.air_info,remark:this.form.remark,itineraries_id:this.itineraries_id});"edit"==this.post_type?Object(o["f"])(this.$route.params.id,e).then((function(e){var a=e.result,i=(a.data,a.extra);t.extra=i})).catch((function(e){e.response&&t.$refs.observer.setErrors(e)})).finally((function(){t.updateing=!1})):"add"==this.post_type&&Object(o["a"])(e).then((function(e){t.$router.replace({name:"TicketDetail",params:{id:e.result.data.id}})})).catch((function(e){e.response&&t.$refs.observer.setErrors(e)})).finally((function(){t.updateing=!1}))},onDelete:function(){var t=this;this.updateing=!0,Object(o["b"])(this.$route.params.id).then((function(){t.$router.go(-1)})).finally((function(){t.updateing=!1}))},onSelectItinerary:function(t){this.itineraries_id=Object.assign([],t)},beforeUpload:function(t){var e=t.size/1024/1024<2;return e||this.$message.error("Image must smaller than 2MB!"),e},handleRemove:function(t){null!=t&&null!=t.id&&Object(s["a"])(t.id)}}}),_=g,k=(a("e8d3"),Object(p["a"])(_,i,r,!1,null,"748b5205",null));e["a"]=k.exports},"91b6":function(t,e,a){"use strict";a.d(e,"a",(function(){return n}));var i=a("365c"),r=a("b775");function n(t){return Object(r["b"])({url:i["a"].Upload+"".concat(t,"/"),method:"delete"}).then(i["g"]).catch(i["f"])}},"9b6f":function(t,e,a){"use strict";a.d(e,"c",(function(){return n})),a.d(e,"a",(function(){return o})),a.d(e,"e",(function(){return s})),a.d(e,"b",(function(){return l})),a.d(e,"d",(function(){return c}));var i=a("365c"),r=a("b775");function n(t){return Object(r["b"])({url:i["a"].Itinerary,method:"get",params:t})}function o(t){return Object(r["b"])({url:i["a"].Itinerary,method:"post",data:t}).then(i["e"]).catch(i["d"])}function s(t,e){return Object(r["b"])({url:i["a"].Itinerary+"".concat(t,"/"),method:"patch",data:e}).then(i["i"]).catch(i["h"])}function l(t,e){return Object(r["b"])({url:i["a"].Itinerary+"".concat(t,"/"),method:"delete"}).then(i["g"]).catch(i["f"])}function c(t){return Object(r["b"])({url:i["a"].ItineraryHistory,method:"get",params:t})}},e8d3:function(t,e,a){"use strict";var i=a("2a9d"),r=a.n(i);r.a}}]);