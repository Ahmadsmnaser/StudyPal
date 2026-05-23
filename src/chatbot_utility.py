import os


working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

def get_chapter_list(selected_subject):

    if selected_subject == "Operating_System":
        subject_name = selected_subject
        chapters_dir = f"{parent_dir}/data/{subject_name}"
        chapters_list = os.listdir(chapters_dir)
        # remove ".txt / .pdf / ..."  from each string in the list
        chapters_list = [x[:-4] for x in chapters_list]
        def sort_key(x):
            try:
                return (0, int(x.split('.')[0]))
            except ValueError:
                return (1, x)
                
        chapters_list.sort(key=sort_key)
        return chapters_list

        