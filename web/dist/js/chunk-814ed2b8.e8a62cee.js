(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-814ed2b8"],{"93b6":function(e,t,a){"use strict";var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("a-card",[a("div",{staticClass:"table-page-search-wrapper"},[a("form-validate",{attrs:{layout:"inline",form:e.queryParam}},[a("a-row",{attrs:{gutter:24}},[a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Role"}},[a("a-select",{on:{change:function(){return e.$refs.table.refresh()}},model:{value:e.queryParam.role,callback:function(t){e.$set(e.queryParam,"role",t)},expression:"queryParam.role"}},[a("a-select-option",{key:"0",attrs:{value:0}},[e._v("All")]),e._l(e.extra.role,(function(t){return a("a-select-option",{key:t.id,attrs:{value:t.id}},[e._v(" "+e._s(t.name))])}))],2)],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Department"}},[a("a-select",{on:{change:function(){return e.$refs.table.refresh()}},model:{value:e.queryParam.department,callback:function(t){e.$set(e.queryParam,"department",t)},expression:"queryParam.department"}},[a("a-select-option",{key:"0",attrs:{value:0}},[e._v("All")]),e._l(e.extra.department,(function(t){return a("a-select-option",{key:t.id,attrs:{value:t.id}},[e._v(" "+e._s(t.name))])}))],2)],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Staff"}},[a("a-select",{on:{change:function(){return e.$refs.table.refresh()}},model:{value:e.queryParam.is_staff,callback:function(t){e.$set(e.queryParam,"is_staff",t)},expression:"queryParam.is_staff"}},[a("a-select-option",{key:"0",attrs:{value:0}},[e._v("All")]),a("a-select-option",{key:"1",attrs:{value:1}},[e._v("Yes")]),a("a-select-option",{key:"2",attrs:{value:2}},[e._v("No")])],1)],1)],1),a("a-col",{attrs:{md:6,sm:24}},[a("form-item-validate",{attrs:{label:"Active"}},[a("a-select",{on:{change:function(){return e.$refs.table.refresh()}},model:{value:e.queryParam.is_active,callback:function(t){e.$set(e.queryParam,"is_active",t)},expression:"queryParam.is_active"}},[a("a-select-option",{key:"0",attrs:{value:0}},[e._v("All")]),a("a-select-option",{key:"1",attrs:{value:1}},[e._v("Yes")]),a("a-select-option",{key:"2",attrs:{value:2}},[e._v("No")])],1)],1)],1),a("a-col",{attrs:{md:24,sm:24}},[a("form-item-validate",[a("a-input-search",{attrs:{placeholder:"E.g Name, Email, Passport No.","enter-button":"Search"},on:{search:function(){return e.$refs.table.refresh()}},model:{value:e.queryParam.search,callback:function(t){e.$set(e.queryParam,"search",t)},expression:"queryParam.search"}})],1)],1)],1)],1)],1),a("s-table",{ref:"table",attrs:{size:"default",rowKey:function(e){return e.id},columns:e.columns,data:e.loadData,pageURI:!0,showPagination:"auto",bordered:""},scopedSlots:e._u([{key:"roles",fn:function(t){return e._l(t,(function(t){return a("div",{key:t.id},[a("span",[e._v(e._s(t.name))])])}))}},{key:"department",fn:function(t){return[t?a("span",[e._v(e._s(t.name))]):e._e()]}},{key:"active",fn:function(e){return[a("a-checkbox",{attrs:{checked:e,disabled:""}})]}},{key:"staff",fn:function(e){return[a("a-checkbox",{attrs:{checked:e,disabled:""}})]}},{key:"action",fn:function(t){return[e.modal?[a("a",{on:{click:function(){return e.$emit("select",t)}}},[e._v("Select")])]:[a("router-link",{attrs:{to:{name:"UserDetail",params:{id:t.id}}}},[a("span",[e._v("Detail")])])]]}}])})],1)},n=[],s=a("2af9"),o=a("c24f"),l={components:{STable:s["d"],FormValidate:s["c"],FormItemValidate:s["b"]},props:{modal:{type:Boolean,default:!1}},data:function(){var e=this;return{extra:{},form:{},queryParam:{role:0,department:0,is_staff:0,is_active:0},columns:[{title:"ID",dataIndex:"id",align:"center",width:"80px",sorter:!0},{title:"Email",dataIndex:"email",align:"center",sorter:!0},{title:"Name",dataIndex:"name",align:"center"},{title:"Passport No",dataIndex:"passport_no",align:"center"},{title:"Role",dataIndex:"roles",scopedSlots:{customRender:"roles"},align:"center"},{title:"Department",dataIndex:"department",scopedSlots:{customRender:"department"},align:"center"},{title:"Staff",dataIndex:"is_staff",width:"100px",scopedSlots:{customRender:"staff"},align:"center",sorter:!0},{title:"Active",dataIndex:"is_active",width:"100px",scopedSlots:{customRender:"active"},align:"center",sorter:!0},{title:"Action",width:"100px",scopedSlots:{customRender:"action"},align:"center"}],loadData:function(t){return Object(o["e"])(Object.assign(t,Object.assign({},e.queryParam,{role:0!=e.queryParam.role?e.queryParam.role:null,department:0!=e.queryParam.department?e.queryParam.department:null,is_staff:0!=e.queryParam.is_staff?1==e.queryParam.is_staff:null,is_active:0!=e.queryParam.is_active?1==e.queryParam.is_active:null}))).then((function(t){var a=t.result,r=a.data,n=a.extra;return e.extra=Object.assign({},n),r}))}}}},c=l,i=a("2877"),u=Object(i["a"])(c,r,n,!1,null,null,null);t["a"]=u.exports},c24f:function(e,t,a){"use strict";a.d(t,"e",(function(){return s})),a.d(t,"d",(function(){return o})),a.d(t,"f",(function(){return l})),a.d(t,"a",(function(){return c})),a.d(t,"b",(function(){return i})),a.d(t,"g",(function(){return u})),a.d(t,"c",(function(){return d}));var r=a("365c"),n=a("b775");function s(e){return Object(n["b"])({url:r["a"].User,method:"get",params:e})}function o(e){return Object(n["b"])({url:r["a"].User+"".concat(e,"/"),method:"get"})}function l(e,t){return Object(n["b"])({url:r["a"].ResetPassword(e),method:"post",data:t})}function c(e){return Object(n["b"])({url:r["a"].ChangePassword,method:"post",data:e})}function i(e){return Object(n["b"])({url:r["a"].User,method:"post",data:e}).then(r["e"]).catch(r["d"])}function u(e,t){return Object(n["b"])({url:r["a"].User+"".concat(e,"/"),method:"patch",data:t}).then(r["i"]).catch(r["h"])}function d(e,t){return Object(n["b"])({url:r["a"].User+"".concat(e,"/"),method:"delete"}).then(r["g"]).catch(r["f"])}},d3f8:function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("page-header-wrapper",[a("table-list")],1)},n=[],s=a("93b6"),o={components:{TableList:s["a"]}},l=o,c=a("2877"),i=Object(c["a"])(l,r,n,!1,null,null,null);t["default"]=i.exports}}]);