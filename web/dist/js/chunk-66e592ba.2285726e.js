(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-66e592ba"],{bdc7:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("page-header-wrapper",[n("a-card",[n("s-table",{ref:"table",attrs:{size:"default",rowKey:function(t){return t.id},columns:t.columns,data:t.loadData,showPagination:"auto",pageURI:!0,bordered:""},scopedSlots:t._u([{key:"action",fn:function(e){return[[n("router-link",{directives:[{name:"action",rawName:"v-action:view_group",arg:"view_group"}],attrs:{to:{name:"RoleDetail",params:{id:e.id}}}},[n("span",[t._v("Detail")])])]]}}])})],1)],1)},r=[],c=n("2af9"),o=n("cc5e"),u={components:{STable:c["d"]},data:function(){var t=this;return{extra:{},queryParam:{name:void 0},columns:[{title:"ID",dataIndex:"id",align:"center",width:"80px",sorter:!0},{title:"Name",dataIndex:"name",align:"center"},{title:"Action",width:"100px",scopedSlots:{customRender:"action"},align:"center"}],loadData:function(e){return Object(o["d"])(Object.assign(e,Object.assign({},t.queryParam,{}))).then((function(t){var e=t.result,n=e.data;e.extra;return n}))}}}},i=u,d=n("2877"),l=Object(d["a"])(i,a,r,!1,null,null,null);e["default"]=l.exports},cc5e:function(t,e,n){"use strict";n.d(e,"d",(function(){return c})),n.d(e,"c",(function(){return o})),n.d(e,"a",(function(){return u})),n.d(e,"e",(function(){return i})),n.d(e,"b",(function(){return d}));var a=n("365c"),r=n("b775");function c(t){return Object(r["b"])({url:a["a"].Role,method:"get",params:t})}function o(t){return Object(r["b"])({url:a["a"].Role+"".concat(t,"/"),method:"get"})}function u(t){return Object(r["b"])({url:a["a"].Role,method:"post",data:t}).then(a["e"]).catch(a["d"])}function i(t,e){return Object(r["b"])({url:a["a"].Role+"".concat(t,"/"),method:"patch",data:e}).then(a["i"]).catch(a["h"])}function d(t,e){return Object(r["b"])({url:a["a"].Role+"".concat(t,"/"),method:"delete"}).then(a["g"]).catch(a["f"])}}}]);