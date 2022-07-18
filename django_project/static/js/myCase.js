// 初始化 项目-模块， 实现二级联动菜单
var SelectInit = function () {
    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");
    var dataList = [];

    // 创建下拉菜单
    function addOptions(cmb, obj) {
        // var option = document.createElement("option");
        // cmb.options.add(option);
        // option.innerHTML = obj.name;
        // option.value = obj.id;
        cmb.options.add(new Option(obj.name, obj.id));
        console.log(obj.name, obj.id);
    }

    // 改变项目，展示对应模块列表
    function changeProject() {
        cmbModule.options.length = 0;
        console.log("项目默认选项的索引", cmbProject.selectedIndex);
        var pid = cmbProject.options[cmbProject.selectedIndex].value;
        console.log("这个才是真的项目id", pid);

        for (let i = 0; i < dataList.length; i++) {
            pid = parseInt(pid);

            if(dataList[i].id === pid) {
                let modules = dataList[i].module_list;
                console.log("对应的模块列表", modules);
                for(let j=0; j< modules.length; j++){
                    addOptions(cmbModule, modules[j]);
                }
            }

        }

    }

    // 获取select对象列表
    function getSelectData() {
        $.get("/manage_case/get_select_data", {}, function (resp) {
            if (resp.status === '10200') {
                dataList = resp.data;

                console.log("想要的数据格式-->", dataList);
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    console.log("每一个项目的数据", dataList[i]);
                    addOptions(cmbProject, dataList[i]);
                }

                // setDefaultOption(cmbProject, defaultProjectId);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            // setDefaultOption(cmbProject, defaultProjectId);

        });
    }

    getSelectData();
};