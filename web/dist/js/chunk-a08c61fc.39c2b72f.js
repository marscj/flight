(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a08c61fc"],{1473:function(t,a,e){},"7c54":function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("page-header-wrapper",[e("form-validate",{ref:"observer",attrs:{form:t.form}},[e("a-card",{staticClass:"card",attrs:{loading:t.loading,bordered:!1}},[e("form-item-validate",{attrs:{label:"Photo"}},[e("a-upload",{staticClass:"avatar-uploader",attrs:{name:"avatar","list-type":"picture","show-upload-list":!1,"before-upload":t.beforeUpload,"custom-request":t.customRequest}},[e("a-avatar",{attrs:{src:t.form.avatar.medium,size:128,alt:"avatar",icon:"user"}})],1)],1),e("a-row",{staticClass:"form-row",attrs:{gutter:16}},[e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Email",vid:"Email"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.email,callback:function(a){t.$set(t.form,"email",a)},expression:"form.email"}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Password",vid:"password"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.password,callback:function(a){t.$set(t.form,"password",a)},expression:"form.password"}},[e("a-icon",{attrs:{slot:"addonAfter",type:"lock"},on:{click:function(){t.$refs.modal.setVisible(!0)}},slot:"addonAfter"})],1)],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"First Name",vid:"first_name"}},[e("a-input",{model:{value:t.form.first_name,callback:function(a){t.$set(t.form,"first_name",a)},expression:"form.first_name"}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Last Name",vid:"last_name"}},[e("a-input",{model:{value:t.form.last_name,callback:function(a){t.$set(t.form,"last_name",a)},expression:"form.last_name"}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Department",vid:"department_id"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.department,callback:function(a){t.$set(t.form,"department",a)},expression:"form.department"}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Role",vid:"role_id"}},[e("a-input",{attrs:{value:t.form.roles.map((function(t){return t.name})).join(" "),disabled:""}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Active",vid:"is_active",help:"Whether the account is available"}},[e("a-checkbox",{attrs:{disabled:""},model:{value:t.form.is_active,callback:function(a){t.$set(t.form,"is_active",a)},expression:"form.is_active"}})],1)],1),e("a-col",{attrs:{lg:12,md:12,sm:24}},[e("form-item-validate",{attrs:{label:"Staff",vid:"is_staff",help:"Used to log in to the back-end website"}},[e("a-checkbox",{attrs:{disabled:""},model:{value:t.form.is_staff,callback:function(a){t.$set(t.form,"is_staff",a)},expression:"form.is_staff"}})],1)],1)],1)],1),e("a-row",[e("a-col",{staticClass:"text-right",attrs:{span:24}},[e("a-button",{attrs:{type:"primary",loading:t.uploading,"html-type":"submit"},on:{click:t.submit}},[t._v(" Submit ")])],1)],1)],1),e("change-password",{ref:"modal",attrs:{title:"Rest Password"}})],1)},s=[],o=(e("d3b7"),e("7ded")),n=e("2e12"),i=e("33a3"),l=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("a-modal",{attrs:{title:"Change Password",confirmLoading:t.loading},on:{ok:t.submit},model:{value:t.visible,callback:function(a){t.visible=a},expression:"visible"}},[e("form-validate",{ref:"password"},[e("form-item-validate",{attrs:{label:"New Password",vid:"new_password1"}},[e("a-input-password",{model:{value:t.form.new_password1,callback:function(a){t.$set(t.form,"new_password1",a)},expression:"form.new_password1"}})],1),e("form-item-validate",{attrs:{label:"Repeat Password",vid:"new_password2"}},[e("a-input-password",{model:{value:t.form.new_password2,callback:function(a){t.$set(t.form,"new_password2",a)},expression:"form.new_password2"}})],1)],1)],1)},c=[],m=e("c24f"),d=e("2af9"),f={components:{FormValidate:d["c"],FormItemValidate:d["b"]},data:function(){return{form:{},loading:!1,visible:!1}},methods:{submit:function(){var t=this;this.loading=!0,Object(m["a"])(this.form).then((function(a){t.setVisible(!1)})).catch((function(a){a.response&&t.$refs.password.setErrors(a)})).finally((function(){t.loading=!1}))},setVisible:function(t){var a=this;this.visible=t,this.visible&&(this.form={},this.$nextTick((function(){a.$refs.password.reset()})))}}},u=f,p=e("2877"),b=Object(p["a"])(u,l,c,!1,null,null,null),v=b.exports;var h={components:{FormValidate:n["a"],FormItemValidate:i["a"],ChangePassword:v},data:function(){return{loading:!1,uploading:!1,form:{}}},mounted:function(){this.getUserData()},methods:{getUserData:function(){var t=this;this.loading=!0,Object(o["a"])().then((function(a){var e=a.result;t.form=Object.assign({},e)})).finally((function(){t.loading=!1}))},beforeUpload:function(t){var a="image/jpeg"===t.type||"image/png"===t.type;a||this.$message.error("You can only upload JPG file!");var e=t.size/1024/1024<2;return e||this.$message.error("Image must smaller than 2MB!"),a&&e},customRequest:function(t){var a=this,e=new FormData;e.append("avatar",t.file),Object(o["d"])(e).then((function(t){var e=t.result;a.form=Object.assign({},e)})).catch((function(t){t.response&&a.$refs.observer.setErrors(t.response.data.result)}))},submit:function(){var t=this;this.uploading=!0;var a={first_name:this.form.first_name,last_name:this.form.last_name};Object(o["d"])(a).then((function(a){var e=a.result;t.form=Object.assign({},e)})).catch((function(a){a.response&&t.$refs.observer.setErrors(a.response.data.result)})).finally((function(){t.uploading=!1}))}}},w=h,g=(e("c5f1"),Object(p["a"])(w,r,s,!1,null,null,null));a["default"]=g.exports},c24f:function(t,a,e){"use strict";e.d(a,"e",(function(){return o})),e.d(a,"d",(function(){return n})),e.d(a,"f",(function(){return i})),e.d(a,"a",(function(){return l})),e.d(a,"b",(function(){return c})),e.d(a,"g",(function(){return m})),e.d(a,"c",(function(){return d}));var r=e("365c"),s=e("b775");function o(t){return Object(s["b"])({url:r["a"].User,method:"get",params:t})}function n(t){return Object(s["b"])({url:r["a"].User+"".concat(t,"/"),method:"get"})}function i(t,a){return Object(s["b"])({url:r["a"].ResetPassword(t),method:"post",data:a})}function l(t){return Object(s["b"])({url:r["a"].ChangePassword,method:"post",data:t})}function c(t){return Object(s["b"])({url:r["a"].User,method:"post",data:t}).then(r["e"]).catch(r["d"])}function m(t,a){return Object(s["b"])({url:r["a"].User+"".concat(t,"/"),method:"patch",data:a}).then(r["i"]).catch(r["h"])}function d(t,a){return Object(s["b"])({url:r["a"].User+"".concat(t,"/"),method:"delete"}).then(r["g"]).catch(r["f"])}},c5f1:function(t,a,e){"use strict";var r=e("1473"),s=e.n(r);s.a}}]);